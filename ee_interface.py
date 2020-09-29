""" Interface with GEE
"""

import ee
from qgis.core import QgsProject, QgsRasterLayer, QgsRectangle

from .misc_utils import (geojson_to_wkt, get_gdal_xml, tms_to_gdalurl,
                         write_xmlfile)


def get_ee_image_tms(image):
    try:
        map_id = ee.data.getMapId({'image': image, 'format': 'png'})
        tms = map_id['tile_fetcher'].url_format
    except ee.ee_exception.EEException as err:
        raise RuntimeError(err) # socket.timeout: timed out
    return tms

def get_ee_image_bb(image, proj='EPSG:3857', maxerror=0.001):
    return image.geometry().bounds(maxerror, ee.Projection(proj)).getInfo()

def add_ee_image_layer(imageid, name, date, bands, scale, b_min=None, b_max=None, palette=None, qml=None, extent=None,
                       shown=False, destination=None):
    nbands = len(bands)
    # if nbands > 3:
    #     rgb = ee.Image(imageid).select(bands[0:3])
    #     pan = ee.Image(imageid).select(bands[3])
    #     huesat = rgb.rgbToHsv().select('hue', 'saturation')
    #     image = ee.Image.cat(huesat, pan).hsvToRgb().select([0, 1, 2], bands[0:3])
    #     nbands = 3
    # else:
    image = ee.Image(imageid)
    if not any([b_min, b_max, palette, qml]):
        image_stats = image.select(bands[0:nbands]).reduceRegion(ee.Reducer.minMax(), None, scale, None, None, False, 1.0E13).getInfo()
        b_min = [image_stats[bands[n] + '_min'] for n in range(nbands)]
        b_max = [image_stats[bands[n] + '_max'] for n in range(nbands)]
        # b_min = [image_stats[bands[0] + '_min'], image_stats[bands[1] + '_min'], image_stats[bands[2] + '_min']]
        # b_max = [image_stats[bands[0] + '_max'], image_stats[bands[1] + '_max'], image_stats[bands[2] + '_max']]
    rgb = image.visualize(bands=bands[0:nbands], min=b_min, max=b_max, palette=palette)
    tms = get_ee_image_tms(rgb)
    if extent is None:
        image_geojson = get_ee_image_bb(rgb)
        extent = geojson_to_wkt(image_geojson)
    bb = QgsRectangle.fromWkt(extent)
    url = tms_to_gdalurl(tms)
    xml = get_gdal_xml(url, nbands=nbands+1)
    # vfn = write_vsimem_xml(xml) # changed to named temporary file
    tmp, fn = write_xmlfile(xml, name, dest=destination)
    layer = QgsRasterLayer(fn, name)
    if layer.isValid():
        if qml is not None:
            layer.loadNamedStyle(qml)
        layer.setExtent(bb)
        if tmp:
            layer.setCustomProperty('ee-image', 'MEM')
        else:
            layer.setCustomProperty('ee-image', 'XML')
        layer.setCustomProperty('ee-image-id', imageid)
        layer.setCustomProperty('ee-image-date', date)
        layer.setCustomProperty('ee-image-bands', bands)
        layer.setCustomProperty('ee-image-scale', scale)
        layer.setCustomProperty('ee-image-b_min', b_min)
        layer.setCustomProperty('ee-image-b_max', b_max)
        layer.setCustomProperty('ee-image-palette', palette)
        layer.setCustomProperty('ee-image-qml', qml)
        layer.setCustomProperty('ee-image-wkt', extent)
        # else:
        #     layer.setAbstract(f"ee.Image('{imageid}')")
        # if len(bands) < 4:
        #     try:
        #         layer.setCustomProperty('ee-image-stats', image_stats)
        #     except NameError:
        #         pass
        if date is not None:
            layer.setAbstract(f"ee.Image('{imageid}') \n\nDate: {date}")
        else:
            layer.setAbstract(f"ee.Image('{imageid}')")
        QgsProject.instance().addMapLayer(layer)
        if not shown:
            QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(shown)

def update_ee_image_layer(imageid, bands, b_min=None, b_max=None, palette=None):
    image = ee.Image(imageid)
    rgb = image.visualize(bands=bands, min=b_min, max=b_max, palette=palette)
    tms = get_ee_image_tms(rgb)
    url = tms_to_gdalurl(tms)
    xml = get_gdal_xml(url, nbands=len(bands)+1)
    return xml

# import re
# regex = r"^EPSG:\d+"

def search_ee_collection(collection: str,
                         extent: list,
                         proj: str,
                         startdate: str,
                         enddate: str,
                         cloudfield: str,
                         cloudcover: int,
                         namefield: str,
                         bands=None,
                         limit=5):

    def get_info(image, lst):
        return ee.List(lst).add(ee.List([image.get('system:id'),
                                         image.get(namefield),
                                         ee.Date(image.get('system:time_start')).format('Y-MM-dd')]))

    first = ee.List([])

    roi = ee.Geometry.Rectangle(extent, ee.Projection(proj), False)

    if cloudfield is None:
        images = ee.ImageCollection(collection).filterDate(startdate, enddate).filterBounds(roi) \
                    .limit(limit, 'system:time_start').iterate(get_info, first)
    elif collection == 'ASTER/AST_L1T_003':
        images = ee.ImageCollection(collection).filterDate(startdate, enddate).filterBounds(roi) \
                    .filter(ee.Filter.And(ee.Filter.lt(cloudfield, cloudcover),
                            ee.Filter.listContains('ORIGINAL_BANDS_PRESENT', bands[0]),
                            ee.Filter.listContains('ORIGINAL_BANDS_PRESENT', bands[1]),
                            ee.Filter.listContains('ORIGINAL_BANDS_PRESENT', bands[2]))) \
                    .limit(limit, cloudfield).iterate(get_info, first)
    else:
        images = ee.ImageCollection(collection).filterDate(startdate, enddate).filterBounds(roi) \
                    .filter(ee.Filter.lt(cloudfield, cloudcover)) \
                    .limit(limit, cloudfield).iterate(get_info, first)

    return ee.List(images).getInfo() # ComputedObject need to coarse to List

def download_ee_image_layer(iface, name, imageid, bands, scale, proj, extent=None):

    if extent is None:
        image = ee.Image(imageid).select(bands)
    else:
        roi = ee.Geometry.Rectangle(extent, ee.Projection(proj), False)
        image = ee.Image(imageid).select(bands).clip(roi)

    task = ee.batch.Export.image.toDrive(image=image,
                                         description=name.replace('/', '_'),
                                         folder='qgis_gee_data_catalog',
                                         scale=int(scale), # coarse it to int
                                         crs=proj,
                                         maxPixels=1.0E13)
    task.start()
    status = task.status()
    taskid, state = status['id'], status['state']

    if state == 'COMPLETED':
        iface.messageBar().pushMessage(f'Task id {taskid} is {state}. Please check GDrive')
    else:
        iface.messageBar().pushMessage(f'Task id {taskid} is {state}. Please wait and check GDrive')
