import json
from pprint import pprint as pprint
import pandas as pd
import requests
from config import airvisapi

url = "http://api.airvisual.com/v2/states?country=USA&key="
statescount = []
states = requests.get(url + airvisapi).json()
detailurl = "http://api.airvisual.com/v2/city?city=Los Angeles&state=California&country=USA&key="
detailrequest = requests.get(detailurl + airvisapi).json()
pprint (detailrequest)
# for x in range(50):
#     statescount.append(states["data"][int(x)]["state"])
#     x += 1
# pprint (statescount)