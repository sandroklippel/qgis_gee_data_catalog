""" Read GEE datasets file
"""

import json
import os.path

datasets = os.path.join(os.path.dirname(__file__), "datasets.json")

with open(datasets, "r") as file:
    GEE_DATASETS = json.load(file)
