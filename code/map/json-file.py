# -*- coding: utf-8 -*-
import pandas as pd
import json
from nations import nationDict
from rdflib import *
import urllib as url

g = Graph()
flucht = Namespace('http://www.flucht.github.io/')
g.bind('flucht', flucht)
g.parse('output.xml')

all_years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
predicates = {'hasTotal':flucht.hasTotal, 'hasGDPCapConstant':flucht.hasGDPCapConstant,  'hasGDPCapGrowth':flucht.hasGDPCapGrowth, 'hasIncomeCapConstant':flucht.hasIncomeCapConstant,  'hasIncomeCapGrowth':flucht.hasIncomeCapGrowth, 'hasUnemploymentILO':flucht.hasUnemploymentILO, 'hasUnemploymentNational':flucht.hasUnemploymentNational, 'hasDeathUCDP':flucht.hasDeathUCDP, 'hasDemocracy':flucht.hasDemocracy, 'hasDeathsTerrorism':flucht.hasDeathsTerrorism, 'hasWoundedTerrorism':flucht.hasWoundedTerrorism}

iso = pd.read_csv('datasets/iso-nations.csv', delimiter = ',', skiprows=1, dtype='unicode', names = ['name','alpha-2','alpha-3','country-code','iso_3166-2','region','sub-region','intermediate-region','region-code','sub-region-code','intermediate-region-code'])

JSONfileFinal = 'datasets/geoData-final.json'
if JSONfileFinal:
    with open(JSONfileFinal, 'r') as f:
        geoDataFinal = json.load(f)

geoJSON = {'type':'FeatureCollection','features':[]}

temporary_geoJSON = {}
for index, row in iso.iterrows():
    temporary_geoJSON[nationDict[row['name']]] = {'type':'Feature','properties':{'name':nationDict[row['name']]},'geometry':{}}

for index, row in iso.iterrows():
    nationEncoded = url.quote(nationDict[row['name']])

    for key, every_predicate in predicates.items():
        temporary_geoJSON[nationDict[row['name']]]['properties'][key] = {"total":0}

        count = 0

        for every_year in all_years:
            year = URIRef('http://www.flucht.github.io/' + nationEncoded + '/' + every_year)

            if (year, every_predicate, None) in g:
                count += 1

                temporary_geoJSON[nationDict[row['name']]]['properties'][key][every_year] = g.value(year, every_predicate).toPython()
                temporary_geoJSON[nationDict[row['name']]]['properties'][key]["total"] += g.value(year, every_predicate).toPython()
                temporary_geoJSON[nationDict[row['name']]]['properties'][key]["average"] = temporary_geoJSON[nationDict[row['name']]]['properties'][key]["total"]/count
            else:
                temporary_geoJSON[nationDict[row['name']]]['properties'][key][every_year]  = ""


errors = ['N. Cyprus', 'Bajo Nuevo Bank (Petrel Is.)', 'Serranilla Bank', 'USNB Guantanamo Bay', 'Cyprus U.N. Buffer Zone', 'Dhekelia', 'Baikonur', 'Siachen Glacier', 'Spratly Islands', 'Scarborough Reef', 'Akrotiri', 'Aland', 'Vatican', 'Ashmore and Cartier Is.', 'Coral Sea Is.']

for each_feature in geoDataFinal['features']:
    tmp_nation = each_feature['properties']['name'].encode('utf-8')
    if tmp_nation not in errors:
        if nationDict[tmp_nation] in temporary_geoJSON:
            temporary_geoJSON[nationDict[tmp_nation]]['geometry'] = each_feature['geometry']
        else:
            print(nationDict[tmp_nation])

for each_dict in temporary_geoJSON.values():
    if len(each_dict['geometry']) != 0:
        geoJSON['features'].append(each_dict)
    else:
        print("No geo data available, dumping information.")

with open('datasets/map-data.json', 'w') as outfile:
    json.dump(geoJSON, outfile)
