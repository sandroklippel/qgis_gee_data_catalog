""" Utilities functions
"""

from tempfile import gettempdir
from uuid import uuid4

import ee
from osgeo import gdal, ogr
from qgis.core import QgsRectangle


def get_canvas_proj(iface):
    return iface.mapCanvas().mapSettings().destinationCrs().authid()

def get_canvas_extent(iface):
    extent = iface.mapCanvas().extent()
    xmin = extent.xMinimum()
    ymin = extent.yMinimum()
    xmax = extent.xMaximum()
    ymax = extent.yMaximum()
    return [xmin, ymin, xmax, ymax]

def get_ee_image_tms(image):
    try:
        map_id = ee.data.getMapId({'image': image, 'format': 'png'})
        tms = map_id['tile_fetcher'].url_format
    except ee.ee_exception.EEException:
        raise RuntimeError("\n\nInvalid ee.Image id")
    return tms

def get_ee_image_bb(image, proj='EPSG:3857', maxerror=0.001):
    bb_as_geojson = ee.Element(image).geometry().bounds(maxerror, ee.Projection(proj)).getInfo()
    ogr_geom = ogr.CreateGeometryFromJson(str(bb_as_geojson))
    wkt_geom = ogr_geom.ExportToIsoWkt()
    return QgsRectangle.fromWkt(wkt_geom)

def tms_to_gdalurl(tms):
    return tms.format(x=r'${x}', y=r'${y}', z=r'${z}')

def get_gdal_xml(url):
    cachedir = gettempdir() + '/gdalwmscache'
    xml = f"""<GDAL_WMS>
    <Service name="TMS">
        <ServerUrl>{url}</ServerUrl>
        <SRS>EPSG:3857</SRS>
        <ImageFormat>image/png</ImageFormat>
    </Service>
    <DataWindow>
        <UpperLeftX>-20037508.34</UpperLeftX>
        <UpperLeftY>20037508.34</UpperLeftY>
        <LowerRightX>20037508.34</LowerRightX>
        <LowerRightY>-20037508.34</LowerRightY>
        <TileLevel>19</TileLevel>
        <TileCountX>1</TileCountX>
        <TileCountY>1</TileCountY>
        <YOrigin>top</YOrigin>
    </DataWindow>
    <Projection>EPSG:3857</Projection>
    <BlockSizeX>256</BlockSizeX>
    <BlockSizeY>256</BlockSizeY>
    <BandsCount>4</BandsCount>
    <ZeroBlockHttpCodes>204,303,400,404,500,501</ZeroBlockHttpCodes>
    <ZeroBlockOnServerException>true</ZeroBlockOnServerException>
    <Cache>
        <Path>{cachedir}</Path>
    </Cache>
</GDAL_WMS>
"""
    return xml

def write_vsimem_xml(xml, oldvfn=None):
    gdal.UseExceptions()
    vfn = '/vsimem/ee_image_' + uuid4().hex + '.xml' if oldvfn is None else oldvfn
    gdal.FileFromMemBuffer(vfn, xml)
    return vfn
