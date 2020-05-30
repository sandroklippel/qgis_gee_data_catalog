""" Search and add layers from GEE
"""
import ee
from qgis.core import QgsProject, QgsRasterLayer

from .utils import (get_ee_image_bb, get_ee_image_tms, get_gdal_xml,
                    tms_to_gdalurl, write_vsimem_xml)


def add_ee_image_layer(imageid, name, bands, scale, shown=False):
    image = ee.Image(imageid).visualize(bands)
    tms = get_ee_image_tms(image)
    bb = get_ee_image_bb(image)
    image_wkt = bb.asWktPolygon()
    url = tms_to_gdalurl(tms)
    xml = get_gdal_xml(url)
    vfn = write_vsimem_xml(xml)
    layer = QgsRasterLayer(vfn, name)
    if layer.isValid():
        layer.setExtent(bb)
        layer.setCustomProperty('ee-image', True)
        layer.setCustomProperty('ee-image-id', imageid)
        layer.setCustomProperty('ee-image-bands', bands)
        layer.setCustomProperty('ee-image-scale', scale)
        layer.setCustomProperty('ee-image-wkt', image_wkt)
        layer.setCustomProperty('ee-image-vfn', vfn)
        QgsProject.instance().addMapLayer(layer)
        if not shown:
            QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(shown)

def update_ee_image_layer(imageid, bands, vfn):
    image = ee.Image(imageid).visualize(bands)
    tms = get_ee_image_tms(image)
    url = tms_to_gdalurl(tms)
    xml = get_gdal_xml(url)
    write_vsimem_xml(xml, vfn)

def search_ee_collection(collection: str,
                         extent: list,
                         proj: str,
                         startdate: str,
                         enddate: str,
                         cloudfield: str,
                         cloudcover: int,
                         originalid: str,
                         limit=5):

    def getid(image, lst):
        return ee.List(lst).add(ee.List([image.get('system:id'), image.get(originalid)]))

    first = ee.List([])

    roi = ee.Geometry.Rectangle(extent, ee.Projection(proj), False)

    images = ee.ImageCollection(collection).filterDate(startdate, enddate).filterBounds(roi) \
                  .filter(ee.Filter.lt(cloudfield, cloudcover)) \
                  .limit(limit, cloudfield).iterate(getid, first)

    return ee.List(images).getInfo()

def download_ee_image_layer(iface, name, imageid, bands, scale, proj, extent=None):

    if extent is None:
        image = ee.Image(imageid).select(bands)
    else:
        roi = ee.Geometry.Rectangle(extent, ee.Projection(proj), False)
        image = ee.Image(imageid).select(bands).clip(roi)

    task = ee.batch.Export.image.toDrive(image=image,
                                         description=name,
                                         folder='qgis_gee_data_catalog',
                                         scale=scale,
                                         crs=proj,
                                         maxPixels=1.0E13)
    task.start()
    status = task.status()
    taskid, state = status['id'], status['state']

    if state == 'COMPLETED':
        iface.messageBar().pushMessage(f'Task id {taskid} is {state}. Please check GDrive')
    else:
        iface.messageBar().pushMessage(f'Task id {taskid} is {state}. Please wait and check GDrive')
