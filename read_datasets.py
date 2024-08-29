""" Read GEE datasets file
"""

import json

with open("datasets.json", "r") as file:
    GEE_DATASETS = json.load(file)
