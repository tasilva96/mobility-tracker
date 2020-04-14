import requests
import json
import urllib.request
import pandas as pd
from pandas.io.json import json_normalize

# states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
#           "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
#           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
#           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
#           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

states = ["AL", "AK"]

json_list = []

for i in states:
    with urllib.request.urlopen("https://pastelsky.github.io/covid-19-mobility-tracker/output/US/" + i + "/mobility.json") as url:
        data = json.loads(url.read().decode())
        json_list.append(data)

print(json_list)