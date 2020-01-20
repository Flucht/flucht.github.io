# -*- coding: utf-8 -*-
import pandas as pd
from nations import nationDict

def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

# iso-nations
df = pd.read_csv('datasets/iso-nations.csv', delimiter = ',', skiprows=1, dtype='unicode', names = ['name','alpha-2','alpha-3','country-code','iso_3166-2','region','sub-region','intermediate-region','region-code','sub-region-code','intermediate-region-code'])

iso = sorted(list(df['name'].unique()), key=str.lower)
for nation in iso:
    if nation not in nations:
        print(nation)

# persons_of_concerns
df = pd.read_csv('datasets/unhcr/persons_of_concerns.csv', delimiter = ',', skiprows=1, dtype='unicode', names = ['Year','Country / territory of asylum/residence','Origin','Refugees (incl. refugee-like situations)','Asylum-seekers (pending cases)','Returned refugees','Internally displaced persons (IDPs)','Returned IDPs','Stateless persons','Others of concern','Total Population'])

nations_not_in_iso = 0
nations_not_in_values = []

persons_of_concerns = sorted(list(df['Origin'].unique()), key=str.lower)
# for nation in nations:
#     if nation not in persons_of_concerns:
#         print(nation)
#
# for nation in persons_of_concerns:
#     if nation not in nations.values():
#         nations_not_in_values.append(nation)
#
# for nation in persons_of_concerns:
#     if nation not in iso:
#         if nation not in nations_not_in_values:
#             print(nation)
#             nations_not_in_iso += 1

for nation in persons_of_concerns:
    if nation not in nations:
        print(nation)

# for nation in persons_of_concerns:
#     if nation not in nations:
#         for word in nation.split():
#             for each_nation in nations:
#                 if contains_word(each_nation, word) is True:
#                     print(each_nation, nation)

# for nation in persons_of_concerns:
#     if nation not in nations:
#         nations[nation] = nation
#
# print(len(persons_of_concerns))

# persons_of_concerns
df = pd.read_csv('datasets/world_bank/gdp_constant/API_NY.GDP.MKTP.KD_DS2_en_csv_v2_566086.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

world_bank = sorted(list(df['Country Name'].unique()), key=str.lower)
# for nation in world_bank:
#     if nation not in nations.values():
#         nations_not_in_values.append(nation)
#
# for nation in world_bank:
#     if nation not in iso:
#         if nation not in nations_not_in_values:
#             print(nation)
#             nations_not_in_iso += 1

for nation in world_bank:
    if nation not in nations:
        print(nation)

# for nation in world_bank:
#     if nation not in nations:
#         nations[nation] = nation
#
# print(len(world_bank))

# ucdp/ged191
df = pd.read_csv('datasets/ucdp/ged191.csv', delimiter = ',', skiprows=1, dtype='unicode', names = ['id','year','active_year','type_of_violence','conflict_new_id','conflict_name','dyad_new_id','dyad_name','side_a_new_id','gwnoa','side_a','side_b_new_id','gwnob','side_b','number_of_sources','source_article','source_office','source_date','source_headline','source_original','where_prec','where_coordinates','adm_1','adm_2','latitude','longitude','geom_wkt','priogrid_gid','country','country_id','region','event_clarity','date_prec','date_start','date_end','deaths_a','deaths_b','deaths_civilians','deaths_unknown','low','best','high'])

ucdp = sorted(list(df['country'].unique()), key=str.lower)
# for nation in ucdp:
#     if nation not in nations.values():
#         nations_not_in_values.append(nation)
#
# for nation in ucdp:
#     if nation not in iso:
#         if nation not in nations_not_in_values:
#             print(nation)
#             nations_not_in_iso += 1

for nation in ucdp:
    if nation not in nations:
        print(nation)

# for nation in ucdp:
#     if nation not in nations:
#         nations[nation] = nation

# EIU-Democracy
df = pd.read_csv('datasets/EIU-Democracy.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['geo','name','time','Democracy index (EIU)','Electoral pluralism index (EIU)','Government index (EIU)','Political participation index(EIU)','Political culture index (EIU)','Civil liberties index (EIU)','Change in democracy index (EIU)'])

democracy = sorted(list(df['name'].unique()), key=str.lower)
# for nation in democracy:
#     if nation not in nations.values():
#         nations_not_in_values.append(nation)
#
# for nation in democracy:
#     if nation not in iso:
#         if nation not in nations_not_in_values:
#             print(nation)
#             nations_not_in_iso += 1

for nation in democracy:
    if nation not in nations:
        print(nation)

# for nation in democracy:
#     if nation not in nations:
#         nations[nation] = nation

# Global Terrorism
df = pd.read_csv('datasets/global_terrorism_db/0919dist.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['eventid','iyear','imonth','iday','approxdate','extended','resolution','country','country_txt','region','region_txt','provstate','city','latitude','longitude','specificity','vicinity','location','summary','crit1','crit2','crit3','doubtterr','alternative','alternative_txt','multiple','success','suicide','attacktype1','attacktype1_txt','attacktype2','attacktype2_txt','attacktype3','attacktype3_txt','targtype1','targtype1_txt','targsubtype1','targsubtype1_txt','corp1','target1','natlty1','natlty1_txt','targtype2','targtype2_txt','targsubtype2','targsubtype2_txt','corp2','target2','natlty2','natlty2_txt','targtype3','targtype3_txt','targsubtype3','targsubtype3_txt','corp3','target3','natlty3','natlty3_txt','gname','gsubname','gname2','gsubname2','gname3','gsubname3','motive','guncertain1','guncertain2','guncertain3','individual','nperps','nperpcap','claimed','claimmode','claimmode_txt','claim2','claimmode2','claimmode2_txt','claim3','claimmode3','claimmode3_txt','compclaim','weaptype1','weaptype1_txt','weapsubtype1','weapsubtype1_txt','weaptype2','weaptype2_txt','weapsubtype2','weapsubtype2_txt','weaptype3','weaptype3_txt','weapsubtype3','weapsubtype3_txt','weaptype4','weaptype4_txt','weapsubtype4','weapsubtype4_txt','weapdetail','nkill','nkillus','nkillter','nwound','nwoundus','nwoundte','property','propextent','propextent_txt','propvalue','propcomment','ishostkid','nhostkid','nhostkidus','nhours','ndays','divert','kidhijcountry','ransom','ransomamt','ransomamtus','ransompaid','ransompaidus','ransomnote','hostkidoutcome','hostkidoutcome_txt','nreleased','addnotes','scite1','scite2','scite3','dbsource','INT_LOG','INT_IDEO','INT_MISC','INT_ANY','related'])

nations_not_in_iso = 0
nations_not_in_values[:] = []

terrorism = sorted(list(df['country_txt'].unique()), key=str.lower)
for nation in terrorism:
    if nation not in nations.values():
        nations_not_in_values.append(nation)

for nation in terrorism:
    if nation not in nations:
        print(nation)

# for nation in terrorism:
#     if nation not in nations:
#         nations[nation] = nation
