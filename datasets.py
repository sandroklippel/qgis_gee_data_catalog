""" Imagery collections from Google Earth Engine's public data catalog

Format description
------------------

Dict

Collection: {
    *'id': str, (if absent use collection key)
    'description': 'Detailed  multiline description',
    'bandcombinations':{
        'label1':{
            'bands':[list: n_bands*(str)],
            'scale': int,
            *'suffix': 'str',
            *'min': int,
            *'max': int,
            *'palette': [list str],
            *'qml': 'str'
            },
        'label2':{
            'bands':[list n_bands*(str)],
            'scale': int,
            *'suffix': 'str',
            *'min': int,
            *'max': int,
            *'palette': [list str],
            *'qml': 'str'
            }
    }
    **'namefield': 'str',
    *'availability':[list: str:startdate, str:enddate],
    *'extent':'str' (wkt polygon EPSG:3857)
    *'cloudfield': 'str'
}

* optional
** if absent must be an ee.Image object not an ee.ImageCollection

"""

DN_MIN = [0, 0, 0]
DN_MAX = [255, 255, 255]

GLOBAL_EXTENT = '''POLYGON((-20037508.34278924390673637 -20037508.34278925508260727,
                            20037508.34278924390673637 -20037508.34278925508260727, 
                            20037508.34278924390673637 20037508.34278924390673637, 
                            -20037508.34278924390673637 20037508.34278924390673637, 
                            -20037508.34278924390673637 -20037508.34278925508260727))'''

LC08_SR = {'Natural color (B4-B3-B2)':{
                'bands':['B4', 'B3', 'B2'],
                'scale':30,
                'suffix':'_r4g3b2'},
            'False color (B4-B5-B3)':{
                'bands':['B4', 'B5', 'B3'],
                'scale':30,
                'suffix':'_r4g5b3'},
            'Color infrared (B5-B4-B3)':{
                'bands':['B5', 'B4', 'B3'],
                'scale':30,
                'suffix':'_r5g4b3'},
            'Shortwave infrared (B7-B5-B4)':{
                'bands':['B7', 'B5', 'B4'],
                'scale':30,
                'suffix':'_r7g5b4'},
            'Agriculture (B6-B5-B2)':{
                'bands':['B6', 'B5', 'B2'],
                'scale':30,
                'suffix':'_r6g5b2'},
            'Geology (B7-B6-B2)':{
                'bands':['B7', 'B6', 'B2'],
                'scale':30,
                'suffix':'_r7g6b2'},
            'Bathymetric (B4-B3-B1)':{
                'bands':['B4', 'B3', 'B1'],
                'scale':30,
                'suffix':'_r4g3b1'},
            'False color urban (B7-B6-B4)':{
                'bands':['B7', 'B6', 'B4'],
                'scale':30,
                'suffix':'_r7g6b4'},
            'Atmospheric penetration / Soil (B7-B6-B5)':{
                'bands':['B7', 'B6', 'B5'],
                'scale':30,
                'suffix':'_r7g6b5'},
            'Healthy vegetation (B5-B6-B2)':{
                'bands':['B5', 'B6', 'B2'],
                'scale':30,
                'suffix':'_r5g6b2'},
            'Vegetation analysis 1 (B5-B6-B4)':{
                'bands':['B5', 'B6', 'B4'],
                'scale':30,
                'suffix':'_r5g6b4'},
            'Vegetation analysis 2 (B6-B5-B4)':{
                'bands':['B6', 'B5', 'B4'],
                'scale':30,
                'suffix':'_r6g5b4'},
            'Forestry / Recent harvest areas (B7-B5-B3)':{
                'bands':['B7', 'B5', 'B3'],
                'scale':30,
                'suffix':'_r7g5b3'}}

LC08 = {'Natural color (B4-B3-B2)':{
            'bands':['B4', 'B3', 'B2'],
            'scale':30,
            'suffix':'_r4g3b2'},
        'Panchromatic (B8)':{
            'bands':['B8'],
            'scale':15,
            'suffix':'_pan'},
        'False color (B4-B5-B3)':{
            'bands':['B4', 'B5', 'B3'],
            'scale':30,
            'suffix':'_r4g5b3'},
        'Color infrared (B5-B4-B3)':{
            'bands':['B5', 'B4', 'B3'],
            'scale':30,
            'suffix':'_r5g4b3'},
        'Shortwave infrared (B7-B5-B4)':{
            'bands':['B7', 'B5', 'B4'],
            'scale':30,
            'suffix':'_r7g5b4'},
        'Agriculture (B6-B5-B2)':{
            'bands':['B6', 'B5', 'B2'],
            'scale':30,
            'suffix':'_r6g5b2'},
        'Geology (B7-B6-B2)':{
            'bands':['B7', 'B6', 'B2'],
            'scale':30,
            'suffix':'_r7g6b2'},
        'Bathymetric (B4-B3-B1)':{
            'bands':['B4', 'B3', 'B1'],
            'scale':30,
            'suffix':'_r4g3b1'},
        'False color urban (B7-B6-B4)':{
            'bands':['B7', 'B6', 'B4'],
            'scale':30,
            'suffix':'_r7g6b4'},
        'Atmospheric penetration / Soil (B7-B6-B5)':{
            'bands':['B7', 'B6', 'B5'],
            'scale':30,
            'suffix':'_r7g6b5'},
        'Healthy vegetation (B5-B6-B2)':{
            'bands':['B5', 'B6', 'B2'],
            'scale':30,
            'suffix':'_r5g6b2'},
        'Vegetation analysis 1 (B5-B6-B4)':{
            'bands':['B5', 'B6', 'B4'],
            'scale':30,
            'suffix':'_r5g6b4'},
        'Vegetation analysis 2 (B6-B5-B4)':{
            'bands':['B6', 'B5', 'B4'],
            'scale':30,
            'suffix':'_r6g5b4'},
        'Forestry / Recent harvest areas (B7-B5-B3)':{
            'bands':['B7', 'B5', 'B3'],
            'scale':30,
            'suffix':'_r7g5b3'}}

LE07_SR = {'Natural color (B3-B2-B1)':{
                'bands':['B3', 'B2', 'B1'],
                'scale':30,
                'suffix':'_r3g2b1'},
            'False color (B3-B4-B2)':{
                'bands':['B3', 'B4', 'B2'],
                'scale':30,
                'suffix':'_r3g4b2'},
            'Color infrared (B4-B3-B2)':{
                'bands':['B4', 'B3', 'B2'],
                'scale':30,
                'suffix':'_r4g3b2'},
            'Shortwave infrared (B7-B4-B3)':{
                'bands':['B7', 'B4', 'B3'],
                'scale':30,
                'suffix':'_r7g4b3'},
            'Agriculture (B5-B4-B1)':{
                'bands':['B5', 'B4', 'B1'],
                'scale':30,
                'suffix':'_r5g4b1'},
            'Geology (B7-B5-B1)':{
                'bands':['B7', 'B5', 'B1'],
                'scale':30,
                'suffix':'_r7g5b1'},
            'False color urban (B7-B5-B3)':{
                'bands':['B7', 'B5', 'B3'],
                'scale':30,
                'suffix':'_r7g5b3'},
            'Atmospheric penetration / Soil (B7-B5-B4)':{
                'bands':['B7', 'B5', 'B4'],
                'scale':30,
                'suffix':'_r7g5b4'},
            'Healthy vegetation (B4-B5-B1)':{
                'bands':['B4', 'B5', 'B1'],
                'scale':30,
                'suffix':'_r4g5b1'},
            'Vegetation analysis 1 (B4-B5-B3)':{
                'bands':['B4', 'B5', 'B3'],
                'scale':30,
                'suffix':'_r4g5b3'},
            'Vegetation analysis 2 (B5-B4-B3)':{
                'bands':['B5', 'B4', 'B3'],
                'scale':30,
                'suffix':'_r5g4b3'},
            'Forestry / Recent harvest areas (B7-B4-B2)':{
                'bands':['B7', 'B4', 'B2'],
                'scale':30,
                'suffix':'_r7g4b2'}}

LE07 = {'Natural color (B3-B2-B1)':{
            'bands':['B3', 'B2', 'B1'],
            'scale':30,
            'suffix':'_r3g2b1'},
        'Panchromatic (B8)':{
            'bands':['B8'],
            'scale':15,
            'suffix':'_pan'},
        'False color (B3-B4-B2)':{
            'bands':['B3', 'B4', 'B2'],
            'scale':30,
            'suffix':'_r3g4b2'},
        'Color infrared (B4-B3-B2)':{
            'bands':['B4', 'B3', 'B2'],
            'scale':30,
            'suffix':'_r4g3b2'},
        'Shortwave infrared (B7-B4-B3)':{
            'bands':['B7', 'B4', 'B3'],
            'scale':30,
            'suffix':'_r7g4b3'},
        'Agriculture (B5-B4-B1)':{
            'bands':['B5', 'B4', 'B1'],
            'scale':30,
            'suffix':'_r5g4b1'},
        'Geology (B7-B5-B1)':{
            'bands':['B7', 'B5', 'B1'],
            'scale':30,
            'suffix':'_r7g5b1'},
        'False color urban (B7-B5-B3)':{
            'bands':['B7', 'B5', 'B3'],
            'scale':30,
            'suffix':'_r7g5b3'},
        'Atmospheric penetration / Soil (B7-B5-B4)':{
            'bands':['B7', 'B5', 'B4'],
            'scale':30,
            'suffix':'_r7g5b4'},
        'Healthy vegetation (B4-B5-B1)':{
            'bands':['B4', 'B5', 'B1'],
            'scale':30,
            'suffix':'_r4g5b1'},
        'Vegetation analysis 1 (B4-B5-B3)':{
            'bands':['B4', 'B5', 'B3'],
            'scale':30,
            'suffix':'_r4g5b3'},
        'Vegetation analysis 2 (B5-B4-B3)':{
            'bands':['B5', 'B4', 'B3'],
            'scale':30,
            'suffix':'_r5g4b3'},
        'Forestry / Recent harvest areas (B7-B4-B2)':{
            'bands':['B7', 'B4', 'B2'],
            'scale':30,
            'suffix':'_r7g4b2'}}

GEE_DATASETS = {
    'COPERNICUS/S2_SR': {
        'description': '''Sentinel-2 MSI
Level-2A orthorectified atmospherically corrected surface reflectance.''',
        'bandcombinations':{'True color (TCI_R-TCI_G-TCI_B)':{
                                'bands':['TCI_R', 'TCI_G', 'TCI_B'],
                                'scale':10,
                                'suffix':'_TCI',
                                'min': DN_MIN,
                                'max': DN_MAX},
                            'Natural color (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':10,
                                'suffix':'_r4g3b2'},
                            'False color (B4-B8-B3)':{
                                'bands':['B4', 'B8', 'B3'],
                                'scale':10,
                                'suffix':'_r4g8b3'},
                            'Color infrared (B8-B4-B3)':{
                                'bands':['B8', 'B4', 'B3'],
                                'scale':10,
                                'suffix':'_r8g4b3'},
                            'Shortwave infrared 1 (B12-B8-B4)':{
                                'bands':['B12', 'B8', 'B4'],
                                'scale':10,
                                'suffix':'_r12g8b4'},
                            'Shortwave infrared 2 (B12-B8A-B4)':{
                                'bands':['B12', 'B8A', 'B4'],
                                'scale':10,
                                'suffix':'_r12g8Ab4'},
                            'Shortwave infrared 3 (B12-B8A-B2)':{
                                'bands':['B12', 'B8A', 'B2'],
                                'scale':10,
                                'suffix':'_r12g8Ab2'},
                            'Agriculture 1 (B11-B8-B2)':{
                                'bands':['B11', 'B8', 'B2'],
                                'scale':10,
                                'suffix':'_r11g8b2'},
                            'Agriculture 2 (B11-B8A-B2)':{
                                'bands':['B11', 'B8A', 'B2'],
                                'scale':10,
                                'suffix':'_r11g8Ab2'},
                            'Geology (B12-B11-B2)':{
                                'bands':['B12', 'B11', 'B2'],
                                'scale':10,
                                'suffix':'_r12g11b2'},
                            'Bathymetric (B4-B3-B1)':{
                                'bands':['B4', 'B3', 'B1'],
                                'scale':10,
                                'suffix':'_r4g3b1'},
                            'False color urban (B12-B11-B4)':{
                                'bands':['B12', 'B11', 'B4'],
                                'scale':10,
                                'suffix':'_r12g11b4'},
                            'Atmospheric penetration / Soil (B12-B11-B8A)':{
                                'bands':['B12', 'B11', 'B8A'],
                                'scale':10,
                                'suffix':'_r12g11b8A'},
                            'Healthy vegetation (B8-B11-B2)':{
                                'bands':['B8', 'B11', 'B2'],
                                'scale':10,
                                'suffix':'_r8g11b2'},
                            'Vegetation analysis 1 (B8-B11-B4)':{
                                'bands':['B8', 'B11', 'B4'],
                                'scale':10,
                                'suffix':'_r8g11b4'},
                            'Vegetation analysis 2 (B11-B8-B4)':{
                                'bands':['B11', 'B8', 'B4'],
                                'scale':10,
                                'suffix':'_r11g8b4'},
                            'Forestry / Recent harvest areas (B12-B8-B3)':{
                                'bands':['B12', 'B8', 'B3'],
                                'scale':10,
                                'suffix':'_r12g8b3'},
                            'Scene Classification Map (SCL)':{
                                'bands':['SCL'],
                                'scale':20,
                                'suffix':'_SCL',
                                'qml':'sentinel2_scl'}},
        'availability': ['2017-03-28', None],
        'namefield': 'PRODUCT_ID',
        'cloudfield': 'CLOUDY_PIXEL_PERCENTAGE'
    },
    'COPERNICUS/S2': {
        'description': '''Sentinel-2 MSI
Level-1C orthorectified top-of-atmosphere reflectance.''',
        'bandcombinations':{'Natural color (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':10,
                                'suffix':'_r4g3b2'},
                            'False color (B4-B8-B3)':{
                                'bands':['B4', 'B8', 'B3'],
                                'scale':10,
                                'suffix':'_r4g8b3'},
                            'Color infrared (B8-B4-B3)':{
                                'bands':['B8', 'B4', 'B3'],
                                'scale':10,
                                'suffix':'_r8g4b3'},
                            'Shortwave infrared 1 (B12-B8-B4)':{
                                'bands':['B12', 'B8', 'B4'],
                                'scale':10,
                                'suffix':'_r12g8b4'},
                            'Shortwave infrared 2 (B12-B8A-B4)':{
                                'bands':['B12', 'B8A', 'B4'],
                                'scale':10,
                                'suffix':'_r12g8Ab4'},
                            'Shortwave infrared 3 (B12-B8A-B2)':{
                                'bands':['B12', 'B8A', 'B2'],
                                'scale':10,
                                'suffix':'_r12g8Ab2'},
                            'Agriculture 1 (B11-B8-B2)':{
                                'bands':['B11', 'B8', 'B2'],
                                'scale':10,
                                'suffix':'_r11g8b2'},
                            'Agriculture 2 (B11-B8A-B2)':{
                                'bands':['B11', 'B8A', 'B2'],
                                'scale':10,
                                'suffix':'_r11g8Ab2'},
                            'Geology (B12-B11-B2)':{
                                'bands':['B12', 'B11', 'B2'],
                                'scale':10,
                                'suffix':'_r12g11b2'},
                            'Bathymetric (B4-B3-B1)':{
                                'bands':['B4', 'B3', 'B1'],
                                'scale':10,
                                'suffix':'_r4g3b1'},
                            'False color urban (B12-B11-B4)':{
                                'bands':['B12', 'B11', 'B4'],
                                'scale':10,
                                'suffix':'_r12g11b4'},
                            'Atmospheric penetration / Soil (B12-B11-B8A)':{
                                'bands':['B12', 'B11', 'B8A'],
                                'scale':10,
                                'suffix':'_r12g11b8A'},
                            'Healthy vegetation (B8-B11-B2)':{
                                'bands':['B8', 'B11', 'B2'],
                                'scale':10,
                                'suffix':'_r8g11b2'},
                            'Vegetation analysis 1 (B8-B11-B4)':{
                                'bands':['B8', 'B11', 'B4'],
                                'scale':10,
                                'suffix':'_r8g11b4'},
                            'Vegetation analysis 2 (B11-B8-B4)':{
                                'bands':['B11', 'B8', 'B4'],
                                'scale':10,
                                'suffix':'_r11g8b4'},
                            'Forestry / Recent harvest areas (B12-B8-B3)':{
                                'bands':['B12', 'B8', 'B3'],
                                'scale':10,
                                'suffix':'_r12g8b3'}},
        'namefield': 'PRODUCT_ID',
        'availability': ['2015-06-23', None],
        'cloudfield': 'CLOUDY_PIXEL_PERCENTAGE'
    },
    'LANDSAT/LC08/C01/T1_SR': {
        'description': '''Landsat 8 OLI
Atmospherically corrected surface reflectance - Tier 1.''',
        'bandcombinations': LC08_SR,
        'namefield': 'LANDSAT_ID',
        'availability': ['2013-04-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LC08/C01/T2_SR': {
        'description': '''Landsat 8 OLI
Atmospherically corrected surface reflectance - Tier 2.''',
        'bandcombinations': LC08_SR,
        'namefield': 'LANDSAT_ID',
        'availability': ['2013-04-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LC08/C01/T1_TOA':{
        'description': '''Landsat 8 OLI
Collection 1 Tier 1 calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations': LC08,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['2013-04-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LC08/C01/T1_RT_TOA':{
        'description': '''Landsat 8 OLI
Collection 1 Tier 1 and Real-Time data calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations': LC08,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['2013-04-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LC08/C01/T2_TOA':{
        'description': '''Landsat 8 OLI
Collection 1 Tier 2 calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations': LC08,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['2013-04-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LC08/C01/T1':{
        'description': '''Landsat 8 OLI
Collection 1 Tier 1 DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations': LC08,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['2013-04-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LC08/C01/T1_RT':{
        'description': '''Landsat 8 OLI
Collection 1 Tier 1 and Real-Time data DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations': LC08,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['2013-04-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LC08/C01/T2':{
        'description': '''Landsat 8 OLI
Collection 1 Tier 2 DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations': LC08,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['2013-04-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LE07/C01/T1_SR': {
        'description': '''Landsat 7 ETM+
Atmospherically corrected surface reflectance - Tier 1.''',
        'bandcombinations': LE07_SR,
        'namefield': 'LANDSAT_ID',
        'availability': ['1999-01-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LE07/C01/T2_SR': {
        'description': '''Landsat 7 ETM+
Atmospherically corrected surface reflectance - Tier 2.''',
        'bandcombinations': LE07_SR,
        'namefield': 'LANDSAT_ID',
        'availability': ['1999-01-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LE07/C01/T1_TOA': {
        'description': '''Landsat 7 ETM+
Collection 1 Tier 1 calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations': LE07,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1999-01-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LE07/C01/T1_RT_TOA': {
        'description': '''Landsat 7 ETM+
Collection 1 Tier 1 and Real-Time data calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations': LE07,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1999-01-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LE07/C01/T2_TOA': {
        'description': '''Landsat 7 ETM+
Collection 1 Tier 2 calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations': LE07,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1999-01-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LE07/C01/T1': {
        'description': '''Landsat 7 ETM+
Collection 1 Tier 1 DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations': LE07,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1999-01-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LE07/C01/T1_RT': {
        'description': '''Landsat 7 ETM+
Collection 1 Tier 1 and Real-Time data DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations': LE07,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1999-01-01', None],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LE07/C01/T2': {
        'description': '''Landsat 7 ETM+
Collection 1 Tier 2 DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations': LE07,
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1999-01-01', None],
        'cloudfield': 'CLOUD_COVER'
    },    
    'LANDSAT/LT05/C01/T1_SR': {
        'description': '''Landsat 5 TM
Atmospherically corrected surface reflectance - Tier 1.''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_ID',
        'availability': ['1984-03-01', '2012-05-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT05/C01/T2_SR': {
        'description': '''Landsat 5 TM
Atmospherically corrected surface reflectance - Tier 2.''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_ID',
        'availability': ['1984-03-01', '2012-05-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT05/C01/T1_TOA': {
        'description': '''Landsat 5 TM
Collection 1 Tier 1 calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1984-03-01', '2012-05-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT05/C01/T2_TOA': {
        'description': '''Landsat 5 TM
Collection 1 Tier 2 calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1984-03-01', '2012-05-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT05/C01/T1': {
        'description': '''Landsat 5 TM
Collection 1 Tier 1 DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1984-03-01', '2012-05-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT05/C01/T2': {
        'description': '''Landsat 5 TM
Collection 1 Tier 2 DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1984-03-01', '2012-05-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LM05/C01/T1': {
        'description': '''Landsat 5 MSS Raw Scenes Tier 1
DN values, representing scaled, calibrated at-sensor radiance.''',
        'bandcombinations':{'False color (B2-B3-B1)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':60,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B3-B2-B1)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':60,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1984-03-01', '2012-05-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LM05/C01/T2': {
        'description': '''Landsat 5 MSS Raw Scenes Tier 2
DN values, representing scaled, calibrated at-sensor radiance.''',
        'bandcombinations':{'False color (B2-B3-B1)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':60,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B3-B2-B1)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':60,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1984-03-01', '2012-05-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT04/C01/T1_SR': {
        'description': '''Landsat 4 TM
Atmospherically corrected surface reflectance - Tier 1.''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_ID',
        'availability': ['1982-08-01', '1993-12-31'], #  August 1982 - December 1993
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT04/C01/T2_SR': {
        'description': '''Landsat 4 TM
Atmospherically corrected surface reflectance - Tier 2.''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_ID',
        'availability': ['1982-08-01', '1993-12-31'], #  August 1982 - December 1993
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT04/C01/T1_TOA': {
        'description': '''Landsat 4 TM
Collection 1 Tier 1 calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1982-08-01', '1993-12-31'], #  August 1982 - December 1993
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT04/C01/T2_TOA': {
        'description': '''Landsat 4 TM
Collection 1 Tier 2 calibrated top-of-atmosphere (TOA) reflectance.''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1982-08-01', '1993-12-31'], #  August 1982 - December 1993
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT04/C01/T1': {
        'description': '''Landsat 4 TM
Collection 1 Tier 1 DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1982-08-01', '1993-12-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT04/C01/T2': {
        'description': '''Landsat 4 TM
Collection 1 Tier 2 DN values, representing scaled, calibrated at-sensor radiance (Raw Scenes).''',
        'bandcombinations':{'Natural color (B3-B2-B1)':{
                                'bands':['B3', 'B2', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g2b1'},
                            'False color (B3-B4-B2)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B4-B3-B2)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3b2'},
                            'Shortwave infrared (B7-B4-B3)':{
                                'bands':['B7', 'B4', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g4b3'},
                            'Agriculture (B5-B4-B1)':{
                                'bands':['B5', 'B4', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b1'},
                            'Geology (B7-B5-B1)':{
                                'bands':['B7', 'B5', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b1'},
                            'False color urban (B7-B5-B3)':{
                                'bands':['B7', 'B5', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b3'},
                            'Atmospheric penetration / Soil (B7-B5-B4)':{
                                'bands':['B7', 'B5', 'B4'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g5b4'},
                            'Healthy vegetation (B4-B5-B1)':{
                                'bands':['B4', 'B5', 'B1'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g5b1'},
                            'Vegetation analysis 1 (B4-B5-B3)':{
                                'bands':['B4', 'B5', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g5b3'},
                            'Vegetation analysis 2 (B5-B4-B3)':{
                                'bands':['B5', 'B4', 'B3'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b3'},
                            'Forestry / Recent harvest areas (B7-B4-B2)':{
                                'bands':['B7', 'B4', 'B2'],
                                'scale':30,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r7g4b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1982-08-01', '1993-12-31'],
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LM04/C01/T1': {
        'description': '''Landsat 4 MSS Raw Scenes Tier 1
DN values, representing scaled, calibrated at-sensor radiance.''',
        'bandcombinations':{'False color (B2-B3-B1)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':60,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B3-B2-B1)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':60,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1982-08-01', '1993-12-31'], #   1982-08-22 - 1993-12-14
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LM04/C01/T2': {
        'description': '''Landsat 4 MSS Raw Scenes Tier 2
DN values, representing scaled, calibrated at-sensor radiance.''',
        'bandcombinations':{'False color (B2-B3-B1)':{
                                'bands':['B3', 'B4', 'B2'],
                                'scale':60,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3g4b2'},
                            'Color infrared (B3-B2-B1)':{
                                'bands':['B4', 'B3', 'B2'],
                                'scale':60,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3b2'}},
        'namefield': 'LANDSAT_PRODUCT_ID',
        'availability': ['1982-08-01', '1993-12-31'], #   1982-08-22 - 1993-12-14
        'cloudfield': 'CLOUD_COVER'
    },
    'ASTER/AST_L1T_003': {
        'description': '''ASTER L1T Radiance
The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) 
is a multispectral imager that was launched on board NASA's Terra spacecraft in December, 1999. 
DN values representing calibrated at-sensor radiance, ortho-rectified and terrain corrected.''',
        'bandcombinations':{'False color (B02-B3N-B01)':{
                                'bands':['B02', 'B3N', 'B01'],
                                'scale':15,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r2g3Nb1'},
                            'Color infrared (B3N-B02-B01)':{
                                'bands':['B3N', 'B02', 'B01'],
                                'scale':15,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3Ng2b1'},
                            'Shortwave infrared (B05-B03-B02)':{
                                'bands':['B05', 'B03', 'B02'],
                                'scale':15,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g3b2'},
                            'False color urban (B05-B04-B02)':{
                                'bands':['B05', 'B04', 'B02'],
                                'scale':15,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b2'},
                            'Atmospheric penetration / Soil (B05-B04-B3N)':{
                                'bands':['B05', 'B04', 'B03N'],
                                'scale':15,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g4b3N'},
                            'Vegetation analysis 1 (B3N-B04-B02)':{
                                'bands':['B3N', 'B04', 'B02'],
                                'scale':15,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r3Ng4b2'},
                            'Vegetation analysis 2 (B04-B3N-B02)':{
                                'bands':['B04', 'B3N', 'B02'],
                                'scale':15,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r4g3Nb2'},
                            'Forestry / Recent harvest areas (B05-B3N-B01)':{
                                'bands':['B05', 'B3N', 'B01'],
                                'scale':15,
                                'max': DN_MAX,
                                'min': DN_MIN,
                                'suffix':'_r5g3Nb1'}},
        'namefield': 'system:id',
        'availability': ['2000-03-04', None],
        'cloudfield': 'CLOUDCOVER'
    },
#     'JAXA/ALOS/AVNIR-2/ORI': {
#         'description': '''This dataset is contains orthorectified imagery from the 
# Advanced Visible and Near Infrared Radiometer type 2 (AVNIR-2) sensor on-board the 
# Advanced Land Observing Satellite (ALOS) "DAICHI".''',
#         'bandcombinations':{'Natural color (B3-B2-B1)':{
#                                 'bands':['B3', 'B2', 'B1'],
#                                 'scale':10,
#                                 'max': DN_MAX,
#                                 'min': DN_MIN,
#                                 'suffix':'_r3g2b1'},
#                             'False color (B3-B4-B2)':{
#                                 'bands':['B3', 'B4', 'B2'],
#                                 'scale':10,
#                                 'max': DN_MAX,
#                                 'min': DN_MIN,
#                                 'suffix':'_r3g4b2'},
#                             'Color infrared (B4-B3-B2)':{
#                                 'bands':['B4', 'B3', 'B2'],
#                                 'scale':10,
#                                 'max': DN_MAX,
#                                 'min': DN_MIN,
#                                 'suffix':'_r4g3b2'}},
#         'namefield': 'system:id',
#         'availability': ['2006-04-26', '2011-04-18']
#     },
#
    'UMD/hansen/global_forest_change_2020_v1_8': {
        'description': '''Hansen Global Forest Change v1.8 (2000-2020).
Time-series analysis of Landsat images in characterizing global forest extent and change.
Source: Hansen, Potapov, Moore, Hancher et al. High-resolution global maps of 21st-century forest cover change. Science 342.6160 (2013): 850-853''',
        'bandcombinations': {'Tree canopy cover for year 2000 (%)':{
                                'bands': ['treecover2000'],
                                'scale': 926,
                                'suffix':'_treecover2000',
                                'qml':'treecover2000'
                            },
                            'Year of gross forest cover loss event':{
                                                    'bands': ['lossyear'],
                                                    'scale': 926,
                                                    'suffix':'_lossyear',
                                                    'qml':'lossyear'
                            }},
        'extent': GLOBAL_EXTENT
    },
#
    'Planet & NICFI Basemaps - Tropical Africa': {
        'id': 'projects/planet-nicfi/assets/basemaps/africa',
        'description': '''PlanetScope Tropical Normalized Analytic Biannual and Monthly series Basemaps.
You must agree to the NICFI terms at https://planet.com/nicfi. 
If you are already a NICFI user and would like to access the Basemaps in GEE, 
you can apply for access at https://www.planet.com/nicfi/?gee=show.''',
        'bandcombinations': {'Natural color (R-G-B)':{
                                'bands':['R', 'G', 'B'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_rgb'},
                            'False color (R-NIR-G)':{
                                'bands':['R', 'N', 'G'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_rng'},
                            'Color infrared (NIR-R-G)':{
                                'bands':['N', 'R', 'G'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_nrg'}},
        'namefield': 'system:index',
        'availability': ['2015-12-01', None],
        'extent': GLOBAL_EXTENT
    },
#
    'Planet & NICFI Basemaps - Tropical Asia': {
        'id': 'projects/planet-nicfi/assets/basemaps/asia',
        'description': '''PlanetScope Tropical Normalized Analytic Biannual and Monthly series Basemaps.
You must agree to the NICFI terms at https://planet.com/nicfi. 
If you are already a NICFI user and would like to access the Basemaps in GEE, 
you can apply for access at https://www.planet.com/nicfi/?gee=show.''',
        'bandcombinations': {'Natural color (R-G-B)':{
                                'bands':['R', 'G', 'B'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_rgb'},
                            'False color (R-NIR-G)':{
                                'bands':['R', 'N', 'G'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_rng'},
                            'Color infrared (NIR-R-G)':{
                                'bands':['N', 'R', 'G'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_nrg'}},
        'namefield': 'system:index',
        'availability': ['2015-12-01', None],
        'extent': GLOBAL_EXTENT
    },
#
    'Planet & NICFI Basemaps - Tropical Americas': {
        'id': 'projects/planet-nicfi/assets/basemaps/americas',
        'description': '''PlanetScope Tropical Normalized Analytic Biannual and Monthly series Basemaps.
You must agree to the NICFI terms at https://planet.com/nicfi. 
If you are already a NICFI user and would like to access the Basemaps in GEE, 
you can apply for access at https://www.planet.com/nicfi/?gee=show.''',
        'bandcombinations': {'Natural color (R-G-B)':{
                                'bands':['R', 'G', 'B'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_rgb'},
                            'False color (R-NIR-G)':{
                                'bands':['R', 'N', 'G'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_rng'},
                            'Color infrared (NIR-R-G)':{
                                'bands':['N', 'R', 'G'],
                                'scale':4.77,
                                'max': [5454, 5454, 5454],
                                'min': [64, 64, 64],
                                'suffix':'_nrg'}},
        'namefield': 'system:index',
        'availability': ['2015-12-01', None],
        'extent': GLOBAL_EXTENT
    },
#
    'JAXA/ALOS/PALSAR/YEARLY/FNF': {
        'description': '''Global PALSAR-2/PALSAR Forest/Non-Forest Map
The global forest/non-forest map (FNF) is generated by classifying the 
SAR image in the global 25m resolution PALSAR-2/PALSAR SAR mosaic so 
that strong and low backscatter pixels are assigned as "forest" and "non-forest", 
respectively. Here, "forest" is defined as the natural forest with the area 
larger than 0.5 ha and forest cover over 10%.''',
        'bandcombinations': {'Forest/Non-Forest landcover classification':{
                                'bands':['fnf'],
                                'scale':25,
                                'qml':'palsar_fnf'}},
        'namefield': 'system:id',
        'availability': ['2015-01-01', '2018-01-02'],
        'extent': GLOBAL_EXTENT
    },
    #
    'JAXA/ALOS/AW3D30/V2_2':{
        'description': '''ALOS World 3D - 30m (AW3D30) is a global digital 
surface model (DSM) dataset with a horizontal resolution of approximately 
30 meters (1 arcsec mesh). The dataset is based on the DSM dataset 
(5-meter mesh version) of the World 3D Topographic Data.''',
        'bandcombinations': {'Elevation':{
                                'bands': ['AVE_DSM'],
                                'scale': 30,
                                'min': -9999,
                                'max': 15355,
                                'palette': ['0000ff', '00ffff', 'ffff00', 'ff0000', 'ffffff']
        }},
        'extent': GLOBAL_EXTENT
    },
    'NASA/JPL/global_forest_canopy_height_2005':{
        'description': '''Global Forest Canopy Height, 2005 
This dataset represents global tree heights based on a fusion of spaceborne-lidar data (2005) 
from the Geoscience Laser Altimeter System (GLAS) and ancillary geospatial data. 
See Simard et al. (2011) for details.''',
        'bandcombinations': {'Tree heights (m)':{
                                'bands': ['1'],
                                'scale': 926,
                                'min': 0,
                                'max': 255
        }},
        'extent': GLOBAL_EXTENT
    },
    'MAPBIOMAS':{
        'id': 'projects/mapbiomas-workspace/public/collection5/mapbiomas_collection50_integration_v1',
        'description': '''MapBiomas Project - Collection 5.0 of the Annual Land Use Land Cover Maps of Brazil.
The MapBiomas project is an initiative of the Climate Observatory co-created and developed by 
a multi-institutional network involving universities, NGOs, and technology companies with the 
purpose of annually map Brazil's land-use and land cover and monitor the changes in the territory.''',
        'bandcombinations':{'Classification 1985':{
                                'bands': ['classification_1985'],
                                'scale': 30,
                                'suffix':'_1985',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1986':{
                                'bands': ['classification_1986'],
                                'scale': 30,
                                'suffix':'_1986',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1987':{
                                'bands': ['classification_1987'],
                                'scale': 30,
                                'suffix':'_1987',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1988':{
                                'bands': ['classification_1988'],
                                'scale': 30,
                                'suffix':'_1988',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1989':{
                                'bands': ['classification_1989'],
                                'scale': 30,
                                'suffix':'_1989',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1990':{
                                'bands': ['classification_1990'],
                                'scale': 30,
                                'suffix':'_1990',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1991':{
                                'bands': ['classification_1991'],
                                'scale': 30,
                                'suffix':'_1991',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1992':{
                                'bands': ['classification_1992'],
                                'scale': 30,
                                'suffix':'_1992',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1993':{
                                'bands': ['classification_1993'],
                                'scale': 30,
                                'suffix':'_1993',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1994':{
                                'bands': ['classification_1994'],
                                'scale': 30,
                                'suffix':'_1994',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1995':{
                                'bands': ['classification_1995'],
                                'scale': 30,
                                'suffix':'_1995',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1996':{
                                'bands': ['classification_1996'],
                                'scale': 30,
                                'suffix':'_1996',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1997':{
                                'bands': ['classification_1997'],
                                'scale': 30,
                                'suffix':'_1997',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1998':{
                                'bands': ['classification_1998'],
                                'scale': 30,
                                'suffix':'_1998',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 1999':{
                                'bands': ['classification_1999'],
                                'scale': 30,
                                'suffix':'_1999',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2000':{
                                'bands': ['classification_2000'],
                                'scale': 30,
                                'suffix':'_2000',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2001':{
                                'bands': ['classification_2001'],
                                'scale': 30,
                                'suffix':'_2001',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2002':{
                                'bands': ['classification_2002'],
                                'scale': 30,
                                'suffix':'_2002',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2003':{
                                'bands': ['classification_2003'],
                                'scale': 30,
                                'suffix':'_2003',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2004':{
                                'bands': ['classification_2004'],
                                'scale': 30,
                                'suffix':'_2004',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2005':{
                                'bands': ['classification_2005'],
                                'scale': 30,
                                'suffix':'_2005',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2006':{
                                'bands': ['classification_2006'],
                                'scale': 30,
                                'suffix':'_2006',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2007':{
                                'bands': ['classification_2007'],
                                'scale': 30,
                                'suffix':'_2007',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2008':{
                                'bands': ['classification_2008'],
                                'scale': 30,
                                'suffix':'_2008',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2009':{
                                'bands': ['classification_2009'],
                                'scale': 30,
                                'suffix':'_2009',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2010':{
                                'bands': ['classification_2010'],
                                'scale': 30,
                                'suffix':'_2010',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2011':{
                                'bands': ['classification_2011'],
                                'scale': 30,
                                'suffix':'_2011',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2012':{
                                'bands': ['classification_2012'],
                                'scale': 30,
                                'suffix':'_2012',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2013':{
                                'bands': ['classification_2013'],
                                'scale': 30,
                                'suffix':'_2013',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2014':{
                                'bands': ['classification_2014'],
                                'scale': 30,
                                'suffix':'_2014',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2015':{
                                'bands': ['classification_2015'],
                                'scale': 30,
                                'suffix':'_2015',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2016':{
                                'bands': ['classification_2016'],
                                'scale': 30,
                                'suffix':'_2016',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2017':{
                                'bands': ['classification_2017'],
                                'scale': 30,
                                'suffix':'_2017',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2018':{
                                'bands': ['classification_2018'],
                                'scale': 30,
                                'suffix':'_2018',
                                'qml': 'mapbiomas-legend-collection50'},
                            'Classification 2019':{
                                'bands': ['classification_2019'],
                                'scale': 30,
                                'suffix':'_2019',
                                'qml': 'mapbiomas-legend-collection50'}
                            },
        'extent': '''POLYGON ((-8298202.37922298 -4375910.03333974,
-3415897.61903642 -4375910.03333974,
-3415897.61903642 761195.087234679,
-8298202.37922298 761195.087234679,
-8298202.37922298 -4375910.03333974))'''
    }
}
