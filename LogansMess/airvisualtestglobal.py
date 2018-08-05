import json
from pprint import pprint as pprint
import pandas as pd
import requests
from config import airvisapi

airvisurl = "http://api.airvisual.com/v2/countries?key="
finalcountry = []
countries = requests.get(airvisurl + airvisapi).json()
for x in range(len(countries["data"])):
    finalcountry.append(countries["data"][int(x)]["country"])

countriesurl = "http://api.population.io:80/1.0/countries"
countriesraw = requests.get(countriesurl).json()
populationurl = "http://api.population.io:80/1.0/population/"
countries = []
for country in countriesraw["countries"]:
    if country in finalcountry:
        countries.append(country)

countriesdf = pd.DataFrame(countries)
population2015 = []
population2016 = []
population2017 = []

for country in countries:
    population = requests.get(populationurl + country + "/2015-12-14/").json()
    population2015.append(population["total_population"]["population"])
countriesdf["2015"] = population2015
for country in countries:
    population = requests.get(populationurl + country + "/2016-12-14/").json()
    population2016.append(population["total_population"]["population"])
countriesdf["2016"] = population2016
for country in countries:
    population = requests.get(populationurl + country + "/2017-12-14/").json()
    population2017.append(population["total_population"]["population"])
countriesdf["2017"] = population2017

with open("2015thru2018globalpoptest.txt", "w") as fd:
    fd.write(str(countriesdf))
print (countriesdf)