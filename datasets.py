""" Imagery collections from Google Earth Engine's public data catalog
"""

GEE_DATASETS = {
    'COPERNICUS/S2_SR': {
        'description': 'Level-2A orthorectified atmospherically corrected surface reflectance.',
        'availability': ['2017-03-28', None],
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
        'bandcombinations':{'Natural Colors (B4-B3-B2)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'False color (B8-B4-B3)':[['B8', 'B4', 'B3'], '_r8g4b3'],
                            'False color (B4-B8-B3)':[['B4', 'B8', 'B3'], '_r4g8b3']},
        'bestresolution': 10,
        'originalid': 'PRODUCT_ID',
        'cloudfield': 'CLOUDY_PIXEL_PERCENTAGE'
    },
    'COPERNICUS/S2': {
        'description': 'Level-1C orthorectified top-of-atmosphere reflectance.',
        'availability': ['2015-06-23', None],
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
        'bandcombinations':{'Natural Colors (B4-B3-B2)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'False color (B8-B4-B3)':[['B8', 'B4', 'B3'], '_r8g4b3'],
                            'False color (B4-B8-B3)':[['B4', 'B8', 'B3'], '_r4g8b3']},
        'bestresolution': 10,
        'originalid': 'PRODUCT_ID',
        'cloudfield': 'CLOUDY_PIXEL_PERCENTAGE'
    },
    'LANDSAT/LC08/C01/T1_SR': {
        'description': 'Atmospherically corrected surface reflectance from the Landsat 8 OLI/TIRS sensors - Tier 1.',
        'availability': ['2013-04-01', None],
        'bands':{'B1':'Ultra Blue',
                 'B2':'Blue',
                 'B3':'Green',
                 'B4':'Red',
                 'B5':'NIR',
                 'B6':'SWIR 1',
                 'B7':'SWIR 2'},
        'bandcombinations':{'Natural Colors (B4-B3-B2)':[['B4', 'B3', 'B2'], '_r4g3b2'],
                            'False color (B5-B4-B3)':[['B5', 'B4', 'B3'], '_r5g4b3'],
                            'False color (B4-B5-B3)':[['B4', 'B5', 'B3'], '_r4g5b3']},
        'bestresolution': 30,
        'originalid': 'LANDSAT_ID',
        'cloudfield': 'CLOUD_COVER'
    }
}
