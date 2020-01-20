# -*- coding: utf-8 -*-
import pandas as pd
from rdflib import *
from nations import nationDict
import urllib as url

flucht = Namespace('http://www.flucht.github.io/')
g = Graph()
g.bind('flucht', flucht)

# <loading_data>
persons_of_concerns = pd.read_csv('datasets/unhcr/persons_of_concerns.csv', delimiter = ',', skiprows=1, dtype='unicode', names = ['Year','Country / territory of asylum/residence','Origin','Refugees (incl. refugee-like situations)','Asylum-seekers (pending cases)','Returned refugees','Internally displaced persons (IDPs)','Returned IDPs','Stateless persons','Others of concern','Total Population'])

gdp_capita_constant = pd.read_csv('datasets/world_bank/gdp_capita_constant/API_NY.GDP.PCAP.KD_DS2_en_csv_v2_566077.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

gdp_capita_current = pd.read_csv('datasets/world_bank/gdp_capita_current/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_566054.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

gdp_capita_growth = pd.read_csv('datasets/world_bank/gdp_capita_growth/API_NY.GDP.PCAP.KD.ZG_DS2_en_csv_v2_566212.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

gdp_constant = pd.read_csv('datasets/world_bank/gdp_constant/API_NY.GDP.MKTP.KD_DS2_en_csv_v2_566086.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

gdp_current = pd.read_csv('datasets/world_bank/gdp_current/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_566085.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

gdp_growth = pd.read_csv('datasets/world_bank/gdp_growth/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_566141.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

income_capita_constant = pd.read_csv('datasets/world_bank/income_capita_constant/API_NY.ADJ.NNTY.PC.KD_DS2_en_csv_v2_612897.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

income_capita_current = pd.read_csv('datasets/world_bank/income_capita_current/API_NY.ADJ.NNTY.PC.CD_DS2_en_csv_v2_612891.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

income_capita_growth = pd.read_csv('datasets/world_bank/income_growth/API_NY.ADJ.NNTY.KD.ZG_DS2_en_csv_v2_612901.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

unemployment_ilo_estimate = pd.read_csv('datasets/world_bank/unemployment_ilo_estimate/API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_566104.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

unemployment_national_estimate = pd.read_csv('datasets/world_bank/unemployment_national_estimate/API_SL.UEM.TOTL.NE.ZS_DS2_en_csv_v2_567361.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['Country Name','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

ucdp = pd.read_csv('datasets/ucdp/ged191.csv', delimiter = ',', skiprows=1, dtype='unicode', names = ['id','year','active_year','type_of_violence','conflict_new_id','conflict_name','dyad_new_id','dyad_name','side_a_new_id','gwnoa','side_a','side_b_new_id','gwnob','side_b','number_of_sources','source_article','source_office','source_date','source_headline','source_original','where_prec','where_coordinates','adm_1','adm_2','latitude','longitude','geom_wkt','priogrid_gid','country','country_id','region','event_clarity','date_prec','date_start','date_end','deaths_a','deaths_b','deaths_civilians','deaths_unknown','low','best','high'])

democracy = pd.read_csv('datasets/democracy/eiu-democracy.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['geo','name','time','Democracy index (EIU)','Electoral pluralism index (EIU)','Government index (EIU)','Political participation index(EIU)','Political culture index (EIU)','Civil liberties index (EIU)','Change in democracy index (EIU)'])

terrorism = pd.read_csv('datasets/global_terrorism_db/0919dist.csv', delimiter = ';', skiprows=1, dtype='unicode', names = ['eventid','iyear','imonth','iday','approxdate','extended','resolution','country','country_txt','region','region_txt','provstate','city','latitude','longitude','specificity','vicinity','location','summary','crit1','crit2','crit3','doubtterr','alternative','alternative_txt','multiple','success','suicide','attacktype1','attacktype1_txt','attacktype2','attacktype2_txt','attacktype3','attacktype3_txt','targtype1','targtype1_txt','targsubtype1','targsubtype1_txt','corp1','target1','natlty1','natlty1_txt','targtype2','targtype2_txt','targsubtype2','targsubtype2_txt','corp2','target2','natlty2','natlty2_txt','targtype3','targtype3_txt','targsubtype3','targsubtype3_txt','corp3','target3','natlty3','natlty3_txt','gname','gsubname','gname2','gsubname2','gname3','gsubname3','motive','guncertain1','guncertain2','guncertain3','individual','nperps','nperpcap','claimed','claimmode','claimmode_txt','claim2','claimmode2','claimmode2_txt','claim3','claimmode3','claimmode3_txt','compclaim','weaptype1','weaptype1_txt','weapsubtype1','weapsubtype1_txt','weaptype2','weaptype2_txt','weapsubtype2','weapsubtype2_txt','weaptype3','weaptype3_txt','weapsubtype3','weapsubtype3_txt','weaptype4','weaptype4_txt','weapsubtype4','weapsubtype4_txt','weapdetail','nkill','nkillus','nkillter','nwound','nwoundus','nwoundte','property','propextent','propextent_txt','propvalue','propcomment','ishostkid','nhostkid','nhostkidus','nhours','ndays','divert','kidhijcountry','ransom','ransomamt','ransomamtus','ransompaid','ransompaidus','ransomnote','hostkidoutcome','hostkidoutcome_txt','nreleased','addnotes','scite1','scite2','scite3','dbsource','INT_LOG','INT_IDEO','INT_MISC','INT_ANY','related'])
# </loading_data>

# <building_graph>
#############
### UNHCR ###
#############
for index, row in persons_of_concerns.iterrows():
    if (int(row['Year']) >= 2008 and int(row['Year']) <= 2018) and (nationDict[row['Origin']] != 'Unknown') and (row['Total Population'] != '*'):
        nationEncoded = url.quote(nationDict[row['Origin']])
        nation = URIRef('http://www.flucht.github.io/' + nationEncoded)
        year = URIRef('http://www.flucht.github.io/' + nationEncoded + '/' + str(row['Year']))
        if (year, flucht.hasTotal, None) in g:
            new_value = int(g.value(year, flucht.hasTotal)) + int(row['Total Population'])
            g.set((year, flucht.hasTotal, Literal(new_value)))
        else:
            g.add((nation, flucht.hasYear, year))
            g.add((year, flucht.hasTotal, Literal(int(row['Total Population']))))


##################
### World Bank ###
##################
columns = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']

def worldBank(file, predicate):
    for index, row in file.iterrows():
        nationEncoded = url.quote(nationDict[row['Country Name']])
        nation = URIRef('http://www.flucht.github.io/' + nationEncoded)
        for item in columns:
            if (pd.isnull(row[item]) is False) and (nationDict[row['Country Name']] != 'Unknown'):
                year = URIRef('http://www.flucht.github.io/' + nationEncoded + '/' + item)
                g.add((nation, flucht.hasYear, year))
                g.add((year, predicate, Literal(float(row[item]))))

worldBank(gdp_capita_constant, flucht.hasGDPCapConstant)
worldBank(gdp_capita_current, flucht.hasGDPCapCurrent)
worldBank(gdp_capita_growth, flucht.hasGDPCapGrowth)
worldBank(gdp_constant, flucht.hasGDPConstant)
worldBank(gdp_current, flucht.hasGDPCurrent)
worldBank(gdp_growth, flucht.hasGDPGrowth)
worldBank(income_capita_constant, flucht.hasIncomeCapConstant)
worldBank(income_capita_current, flucht.hasIncomeCapCurrent)
worldBank(income_capita_growth, flucht.hasIncomeCapGrowth)
worldBank(unemployment_ilo_estimate, flucht.hasUnemploymentILO)
worldBank(unemployment_national_estimate, flucht.hasUnemploymentNational)


############
### UCDP ###
############
for index, row in ucdp.iterrows():
    nationEncoded = url.quote(nationDict[row['country']])
    if (int(row['year']) >= 2008 and int(row['year']) <= 2018) and (nationDict[row['country']] != 'Unknown'):
        nation = URIRef('http://www.flucht.github.io/' + nationEncoded)
        year = URIRef('http://www.flucht.github.io/' + nationEncoded + '/' + str(row['year']))

        if pd.isnull(row['best']) is False:
            if (year, flucht.hasDeathUCDP, None) in g:
                new_value = int(g.value(year, flucht.hasDeathUCDP)) + int(row['best'])
                g.set((year, flucht.hasDeathUCDP, Literal(new_value)))
            else:
                g.add((nation, flucht.hasYear, year))
                g.add((year, flucht.hasDeathUCDP, Literal(int(row['best']))))


#############################
### EIU Democracy Indices ###
#############################
for index, row in democracy.iterrows():
    nationEncoded = url.quote(nationDict[row['name']])
    if (int(row['time']) >= 2008 and int(row['time']) <= 2018) and (nationDict[row['name']] != 'Unknown'):
        nation = URIRef('http://www.flucht.github.io/' + nationEncoded)
        year = URIRef('http://www.flucht.github.io/' + nationEncoded + '/' + str(row['time']))
        g.add((nation, flucht.hasYear, year))

        # g.add((year, flucht.hasDemocracy, Literal(row['Democracy index (EIU)'])))
        # g.add((year, flucht.hasPluralism, Literal(row['Electoral pluralism index (EIU)'])))
        # g.add((year, flucht.hasGovernment, Literal(row['Government index (EIU)'])))
        # g.add((year, flucht.hasParticipation, Literal(row['Political participation index(EIU)'])))
        # g.add((year, flucht.hasCulture, Literal(row['Political culture index (EIU)'])))
        # g.add((year, flucht.hasLiberties, Literal(row['Civil liberties index (EIU)'])))
        # g.add((year, flucht.hasChange, Literal(row['Change in democracy index (EIU)'])))

        # average = (float(row['Democracy index (EIU)'].replace(',','.')) + float(row['Electoral pluralism index (EIU)'].replace(',','.')) + float(row['Government index (EIU)'].replace(',','.')) + float(row['Political participation index(EIU)'].replace(',','.')) + float(row['Political culture index (EIU)'].replace(',','.')) + float(row['Civil liberties index (EIU)'].replace(',','.')) + float(row['Change in democracy index (EIU)'].replace(',','.')))/7

        value = float(row['Democracy index (EIU)'].replace(',','.'))

        g.add((year, flucht.hasDemocracy, Literal(value)))


########################
### Global Terrorism ###
########################
for index, row in terrorism.iterrows():
    nationEncoded = url.quote(nationDict[row['country_txt']])
    if (int(row['iyear']) >= 2008 and int(row['iyear']) <= 2018) and (nationDict[row['country_txt']] != 'Unknown'):
        nation = URIRef('http://www.flucht.github.io/' + nationEncoded)
        year = URIRef('http://www.flucht.github.io/' + nationEncoded + '/' + str(row['iyear']))

        if pd.isnull(row['nkill']) is False:
            if (year, flucht.hasDeathsTerrorism, None) in g:
                new_value = int(g.value(year, flucht.hasDeathsTerrorism)) + int(float(row['nkill'].replace(',','.')))
                g.set((year, flucht.hasDeathsTerrorism, Literal(int(new_value))))
            else:
                g.add((nation, flucht.hasYear, year))
                g.add((year, flucht.hasDeathsTerrorism, Literal(int(float(row['nkill'])))))

        if pd.isnull(row['nwound']) is False:
            if (year, flucht.hasWoundedTerrorism, None) in g:
                new_value = int(g.value(year, flucht.hasWoundedTerrorism)) + int(float(row['nwound'].replace(',','.')))
                g.set((year, flucht.hasWoundedTerrorism, Literal(int(new_value))))
            else:
                g.add((nation, flucht.hasYear, year))
                g.add((year, flucht.hasWoundedTerrorism, Literal(int(float(row['nwound'])))))

# </building_graph>

# <saving>
g.serialize(destination='output.xml', format='xml')
# </saving>
