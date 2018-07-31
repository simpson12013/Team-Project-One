import json
from pprint import pprint as pprint
import pandas as pd
import requests


countriesurl = "http://api.population.io:80/1.0/countries"
countriesraw = requests.get(countriesurl).json()

# http://api.population.io:80/1.0/population/Brazil/2015-12-24/
populationurl = "http://api.population.io:80/1.0/population/"
countrypopulations = {}
exclusions = {"Less developed regions",
            "Less developed regions, excluding China",
            'Less developed regions, excluding least developed countries',
            'Least developed countries',
            "World",
            'AFRICA'}
year = []
countrypopulation = []
countries = []
i = 0
for country in countriesraw["countries"]:
    # for x in exclusions:
    if (country !=  "Less developed regions" 
    and country !=  "Less developed regions, excluding China"
    and country !=  'Less developed regions, excluding least developed countries'
    and country !=  'Least developed countries'
    and country !=  "World"
    and country !=  'AFRICA'
    and country !=  'ASIA'
    and country !=  'Australia/New Zealand'
    and country not in countries):
        countries.append(country)
countriesdf = pd.DataFrame(countries)
populations = []
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

print (countriesdf)
# y = 2015
# while y != 2017.:

#     for country in countries:
#         population = requests.get(populationurl + country + "/" + str(y) + "-12-14/").json()
#         countrypopulation = population["total_population"]["population"]
#     y += 1
