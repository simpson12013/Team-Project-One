import json
from pprint import pprint as pprint
import pandas as pd
import requests
from config import censusapi
from json import loads

# url = "http://api.census.gov/data/timeseries/idb/1year?get=AREA_KM2,NAME,AGE,POP&time=2018&SEX=0"
# request = requests.get(url + censusapi)

# with open("2018globalpopulation.txt", "w") as fd:
#     fd.write(request.text)
data = pd.read_csv("2018globalpopulation.txt")
df = pd.DataFrame(data)
uniquecountries = df["NAME"].unique()
totalpopbycountrydf = pd.DataFrame(uniquecountries)

population = 0
negater = 0

years = []
for x in range(9):
    year = 2010 + x
    years.append(year)


    # totalpopulation = []
    # for i in range(len(df)):
    #     population += df["POP"][i]
    #     if df["AGE"][i] == 100:
    #         countrypop = population - negater
    #         negater = population
    #         totalpopulation.append(countrypop)

for year in years:
    dataloop = pd.read_csv(f"{year}globalpopulation.txt")
    dfloop = pd.DataFrame(dataloop)
    totalpopulation = []
    for i in range(len(df)):
        population += dfloop["POP"][i]
        if df["AGE"][i] == 100:
            countrypop = population - negater
            negater = population
            totalpopulation.append(countrypop)

    totalpopbycountrydf[f"{year} Total Population"] = totalpopulation
with open("2010thru2018globaltotalpopulation.txt", "w") as fd:
    fd.write(str(totalpopbycountrydf))