""" Imagery collections from Google Earth Engine's public data catalog
"""

GEE_DATASETS = {
    'COPERNICUS/S2_SR': {
        'description': '''
Sentinel-2 MSI: Multispectral Instrument
Level-2A orthorectified atmospherically corrected surface reflectance.''',
        'bands':{'B2':'Blue',
                 'B3':'Green',
                 'B4':'Red',
                 'B5':'Red Edge 1',
                 'B6':'Red Edge 2',
                 'B7':'Red Edge 3',
                 'B8':'NIR',
                 'B8A':'Red Edge 4',
                 'B11':'SWIR 1',
                 'B12':'SWIR 2'},
        'bandcombinations':{'True color (TCI_R-TCI_G-TCI_B)':[['TCI_R', 'TCI_G', 'TCI_R'], '_r4g3b2'],
                            'Natural color (B4-B3-B2)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'False color (B4-B8-B3)':[['B4', 'B8', 'B8'], '_r4g8b3'],
                            'Color infrared (B8-B4-B3)':[['B8', 'B4', 'B3'], '_r8g4b3'],
                            'Shortwave infrared 1 (B12-B8-B4)':[['B12', 'B8', 'B4'], '_r12g8b4'],
                            'Shortwave infrared 2 (B12-B8A-B4)':[['B12', 'B8A', 'B4'], '_r12g8Ab4'],
                            'Agriculture 1 (B11-B8-B2)':[['B11', 'B8', 'B2'], '_r11g8b2'],
                            'Agriculture 2 (B11-B8A-B2)':[['B11', 'B8A', 'B2'], '_r11g8Ab2'],
                            'Geology (B12-B11-B2)':[['B12', 'B11', 'B2'], '_r12g11b2'],
                            'Bathymetric (B4-B3-B1)':[['B4', 'B3', 'B1'], '_r4g3b1'],
                            'False color urban (B12-B11-B4)':[['B12', 'B11', 'B4'], '_r12g11b4'],
                            'Atmospheric penetration / Soil (B12-B11-B8A)':[['B12', 'B11', 'B8A'], '_r12g11b8A'],
                            'Healthy vegetation (B8-B11-B2)':[['B8', 'B11', 'B2'], '_r8g11b2'],
                            'Vegetation analysis 1 (B8-B11-B4)':[['B8', 'B11', 'B4'], '_r8g11b4'],
                            'Vegetation analysis 2 (B11-B8-B4)':[['B11', 'B8', 'B4'], '_r11g8b4'],
                            'Forestry / Recent harvest areas (B12-B8-B3)':[['B12', 'B8', 'B3'], '_r12g8b3']},
        'bestresolution': 10,
        'availability': ['2017-03-28', None],
        'originalid': 'PRODUCT_ID',
        'cloudfield': 'CLOUDY_PIXEL_PERCENTAGE'
    },
    'COPERNICUS/S2': {
        'description': '''
Sentinel-2 MSI: Multispectral Instrument
Level-1C orthorectified top-of-atmosphere reflectance.''',
        'bands':{'B2':'Blue',
                 'B3':'Green',
                 'B4':'Red',
                 'B5':'Red Edge 1',
                 'B6':'Red Edge 2',
                 'B7':'Red Edge 3',
                 'B8':'NIR',
                 'B8A':'Red Edge 4',
                 'B11':'SWIR 1',
                 'B12':'SWIR 2'},
        'bandcombinations':{'Natural color (B4-B3-B2)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'False color (B4-B8-B3)':[['B4', 'B8', 'B8'], '_r4g8b3'],
                            'Color infrared (B8-B4-B3)':[['B8', 'B4', 'B3'], '_r8g4b3'],
                            'Shortwave infrared 1 (B12-B8-B4)':[['B12', 'B8', 'B4'], '_r12g8b4'],
                            'Shortwave infrared 2 (B12-B8A-B4)':[['B12', 'B8A', 'B4'], '_r12g8Ab4'],
                            'Agriculture 1 (B11-B8-B2)':[['B11', 'B8', 'B2'], '_r11g8b2'],
                            'Agriculture 2 (B11-B8A-B2)':[['B11', 'B8A', 'B2'], '_r11g8Ab2'],
                            'Geology (B12-B11-B2)':[['B12', 'B11', 'B2'], '_r12g11b2'],
                            'Bathymetric (B4-B3-B1)':[['B4', 'B3', 'B1'], '_r4g3b1'],
                            'False color urban (B12-B11-B4)':[['B12', 'B11', 'B4'], '_r12g11b4'],
                            'Atmospheric penetration / Soil (B12-B11-B8A)':[['B12', 'B11', 'B8A'], '_r12g11b8A'],
                            'Healthy vegetation (B8-B11-B2)':[['B8', 'B11', 'B2'], '_r8g11b2'],
                            'Vegetation analysis 1 (B8-B11-B4)':[['B8', 'B11', 'B4'], '_r8g11b4'],
                            'Vegetation analysis 2 (B11-B8A-B4)':[['B11', 'B8A', 'B4'], '_r11g8Ab4'],
                            'Forestry / Recent harvest areas (B12-B8-B3)':[['B12', 'B8', 'B3'], '_r12g8b3']},
        'bestresolution': 10,
        'availability': ['2015-06-23', None],
        'originalid': 'PRODUCT_ID',
        'cloudfield': 'CLOUDY_PIXEL_PERCENTAGE'
    },
    'LANDSAT/LC08/C01/T1_SR': {
        'description': '''
Landsat 8 OLI 
Atmospherically corrected surface reflectance - Tier 1.''',
        'bands':{'B1':'Ultra Blue',
                 'B2':'Blue',
                 'B3':'Green',
                 'B4':'Red',
                 'B5':'NIR',
                 'B6':'SWIR 1',
                 'B7':'SWIR 2'},
        'bandcombinations':{'Natural color (B4-B3-B2)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'False color (B4-B5-B3)':[['B4', 'B5', 'B8'], '_r4g5b3'],
                            'Color infrared (B5-B4-B3)':[['B5', 'B4', 'B3'], '_r5g4b3'],
                            'Shortwave infrared (B7-B5-B4)':[['B7', 'B5', 'B4'], '_r7g5b4'],
                            'Agriculture (B6-B5-B2)':[['B6', 'B5', 'B2'], '_r6g5b2'],
                            'Geology (B7-B6-B2)':[['B7', 'B6', 'B2'], '_r7g6b2'],
                            'Bathymetric (B4-B3-B1)':[['B4', 'B3', 'B1'], '_r4g3b1'],
                            'False color urban (B7-B6-B4)':[['B7', 'B6', 'B4'], '_r7g6b4'],
                            'Atmospheric penetration / Soil (B7-B6-B5)':[['B7', 'B6', 'B5'], '_r7g6b5'],
                            'Healthy vegetation (B5-B6-B2)':[['B5', 'B6', 'B2'], '_r5g6b2'],
                            'Vegetation analysis 1 (B5-B6-B4)':[['B5', 'B6', 'B4'], '_r5g6b4'],
                            'Vegetation analysis 2 (B6-B5-B4)':[['B6', 'B5', 'B4'], '_r6g5b4'],
                            'Forestry / Recent harvest areas (B7-B5-B3)':[['B7', 'B5', 'B3'], '_r7g5b3']},
        'bestresolution': 30,
        'availability': ['2013-04-01', None],
        'originalid': 'LANDSAT_ID',
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LC08/C01/T2_SR': {
        'description': '''
Landsat 8 OLI 
Atmospherically corrected surface reflectance - Tier 2.''',
        'bands':{'B1':'Ultra Blue',
                 'B2':'Blue',
                 'B3':'Green',
                 'B4':'Red',
                 'B5':'NIR',
                 'B6':'SWIR 1',
                 'B7':'SWIR 2'},
        'bandcombinations':{'Natural color (B4-B3-B2)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'False color (B4-B5-B3)':[['B4', 'B5', 'B8'], '_r4g5b3'],
                            'Color infrared (B5-B4-B3)':[['B5', 'B4', 'B3'], '_r5g4b3'],
                            'Shortwave infrared (B7-B5-B4)':[['B7', 'B5', 'B4'], '_r7g5b4'],
                            'Agriculture (B6-B5-B2)':[['B6', 'B5', 'B2'], '_r6g5b2'],
                            'Geology (B7-B6-B2)':[['B7', 'B6', 'B2'], '_r7g6b2'],
                            'Bathymetric (B4-B3-B1)':[['B4', 'B3', 'B1'], '_r4g3b1'],
                            'False color urban (B7-B6-B4)':[['B7', 'B6', 'B4'], '_r7g6b4'],
                            'Atmospheric penetration / Soil (B7-B6-B5)':[['B7', 'B6', 'B5'], '_r7g6b5'],
                            'Healthy vegetation (B5-B6-B2)':[['B5', 'B6', 'B2'], '_r5g6b2'],
                            'Vegetation analysis 1 (B5-B6-B4)':[['B5', 'B6', 'B4'], '_r5g6b4'],
                            'Vegetation analysis 2 (B6-B5-B4)':[['B6', 'B5', 'B4'], '_r6g5b4'],
                            'Forestry / Recent harvest areas (B7-B5-B3)':[['B7', 'B5', 'B3'], '_r7g5b3']},
        'bestresolution': 30,
        'availability': ['2013-04-01', None],
        'originalid': 'LANDSAT_ID',
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT05/C01/T1_SR': {
        'description': '''
Landsat 5 ETM 
Atmospherically corrected surface reflectance - Tier 1.''',
        'bands':{'B1':'Blue',
                 'B2':'Green',
                 'B3':'Red',
                 'B4':'NIR',
                 'B5':'SWIR 1',
                 'B7':'SWIR 2'},
        'bandcombinations':{'Natural color (B3-B2-B1)':[['B3', 'B2', 'B1'], '_r3g2b1'],
                            'False color (B3-B4-B2)':[['B3', 'B4', 'B2'], '_r3g4b2'],
                            'Color infrared (B5-B4-B3)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'Shortwave infrared (B7-B4-B3)':[['B7', 'B4', 'B3'], '_r7g4b3'],
                            'Agriculture (B5-B4-B1)':[['B5', 'B4', 'B1'], '_r5g4b1'],
                            'Geology (B7-B5-B1)':[['B7', 'B5', 'B1'], '_r7g5b1'],
                            'False color urban (B7-B5-B3)':[['B7', 'B5', 'B3'], '_r7g5b3'],
                            'Atmospheric penetration / Soil (B7-B5-B4)':[['B7', 'B5', 'B4'], '_r7g5b4'],
                            'Healthy vegetation (B4-B5-B1)':[['B4', 'B5', 'B1'], '_r4g5b1'],
                            'Vegetation analysis 1 (B4-B5-B3)':[['B4', 'B5', 'B3'], '_r4g5b3'],
                            'Vegetation analysis 2 (B5-B4-B3)':[['B5', 'B4', 'B3'], '_r5g4b3'],
                            'Forestry / Recent harvest areas (B7-B4-B2)':[['B7', 'B4', 'B2'], '_r7g4b2']},
        'bestresolution': 30,
        'availability': ['1984-03-01', '2012-05-31'],
        'originalid': 'LANDSAT_ID',
        'cloudfield': 'CLOUD_COVER'
    },
    'LANDSAT/LT05/C01/T2_SR': {
        'description': '''
Landsat 5 ETM 
Atmospherically corrected surface reflectance - Tier 1.''',
        'bands':{'B1':'Blue',
                 'B2':'Green',
                 'B3':'Red',
                 'B4':'NIR',
                 'B5':'SWIR 1',
                 'B7':'SWIR 2'},
        'bandcombinations':{'Natural color (B3-B2-B1)':[['B3', 'B2', 'B1'], '_r3g2b1'],
                            'False color (B3-B4-B2)':[['B3', 'B4', 'B2'], '_r3g4b2'],
                            'Color infrared (B5-B4-B3)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'Shortwave infrared (B7-B4-B3)':[['B7', 'B4', 'B3'], '_r7g4b3'],
                            'Agriculture (B5-B4-B1)':[['B5', 'B4', 'B1'], '_r5g4b1'],
                            'Geology (B7-B5-B1)':[['B7', 'B5', 'B1'], '_r7g5b1'],
                            'False color urban (B7-B5-B3)':[['B7', 'B5', 'B3'], '_r7g5b3'],
                            'Atmospheric penetration / Soil (B7-B5-B4)':[['B7', 'B5', 'B4'], '_r7g5b4'],
                            'Healthy vegetation (B4-B5-B1)':[['B4', 'B5', 'B1'], '_r4g5b1'],
                            'Vegetation analysis 1 (B4-B5-B3)':[['B4', 'B5', 'B3'], '_r4g5b3'],
                            'Vegetation analysis 2 (B5-B4-B3)':[['B5', 'B4', 'B3'], '_r5g4b3'],
                            'Forestry / Recent harvest areas (B7-B4-B2)':[['B7', 'B4', 'B2'], '_r7g4b2']},
        'bestresolution': 30,
        'availability': ['1984-03-01', '2012-05-31'],
        'originalid': 'LANDSAT_ID',
        'cloudfield': 'CLOUD_COVER'
    }
}
