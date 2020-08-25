""" Misc utilities functions
"""

from tempfile import NamedTemporaryFile, gettempdir
from uuid import uuid4
from xml.dom import minidom

from osgeo import gdal, ogr

gdal.UseExceptions()

def geojson_to_wkt(geojson):
    ogr_geom = ogr.CreateGeometryFromJson(str(geojson))
    wkt_geom = ogr_geom.ExportToIsoWkt()
    return wkt_geom

def tms_to_gdalurl(tms):
    return tms.format(x=r'${x}', y=r'${y}', z=r'${z}')

def get_gdal_xml(url, nbands=4):
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
    <BandsCount>{nbands}</BandsCount>
    <ZeroBlockHttpCodes>204,303,400,404,500,501</ZeroBlockHttpCodes>
    <ZeroBlockOnServerException>true</ZeroBlockOnServerException>
    <Cache>
        <Path>{cachedir}</Path>
    </Cache>
</GDAL_WMS>
"""
    return xml

def write_vsimem_xml(xml):
    vfn = '/vsimem/ee_image_' + uuid4().hex + '.xml'
    gdal.FileFromMemBuffer(vfn, xml)
    return vfn

def write_tempfile_xml(xml):
    with NamedTemporaryFile("w+t", prefix="gee_data_catalog_", suffix=".xml", delete=False) as f:
        print(xml, file=f)
        fn = f.name
    return fn

def replace_tms(xml_file, new_tms):
    dom = minidom.parse(xml_file)
    elem = dom.getElementsByTagName('ServerUrl')
    elem[0].firstChild.nodeValue = new_tms
    with open(xml_file, 'w') as outfile:
        dom.documentElement.writexml(outfile)
