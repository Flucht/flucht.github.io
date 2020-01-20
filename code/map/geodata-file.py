# -*- coding: utf-8 -*-
import pandas as pd
import json
from nations import nationDict

# iso-nations
iso = pd.read_csv('datasets/iso-nations.csv', delimiter = ',', skiprows=1, dtype='unicode', names = ['name','alpha-2','alpha-3','country-code','iso_3166-2','region','sub-region','intermediate-region','region-code','sub-region-code','intermediate-region-code'])

JSONfile = "datasets/geoData.json"
JSONfileLarge = "datasets/geoData-large.json"
JSONfileFinal = "datasets/geoData-final.json"

#Read JSON data into the datastore variable
if JSONfile:
    with open(JSONfile, 'r') as f:
        geoData = json.load(f)

if JSONfileLarge:
    with open(JSONfileLarge, 'r') as f:
        geoDataLarge = json.load(f)

if JSONfileFinal:
    with open(JSONfileFinal, 'r') as f:
        geoDataFinal = json.load(f)

#Use the new datastore datastructure
count = 0
existing_nations = []
# for nation in geoData["features"]:
#     count += 1
#     print(nation["properties"]["name"].encode('utf-8'), count)

# for nation in geoData["features"]:
#     existing_nations.append(nation["properties"]["name"].encode('utf-8'))
#
    # if nation["properties"]["iso_a3"].encode('utf-8') not in set(iso["alpha-3"]):
    #     count += 1
    #     print(nation["properties"]["name"].encode('utf-8'), count)

# parking = []
#
# for nation in geoDataLarge["features"]:
#     if nation["properties"]["name"].encode('utf-8') not in existing_nations:
#         parking.append(nation)
#
# print(len(geoData["features"]))
# geoData["features"].extend(parking)
# print(len(geoData["features"]))
#
# with open('datasets/geoData-final.json', 'w') as outfile:
#     json.dump(geoData, outfile)

for nation in geoDataFinal["features"]:
    if nation["properties"]["name"].encode('utf-8') not in nationDict.keys():
        count += 1
        print(nation["properties"]["name"].encode('utf-8'))
