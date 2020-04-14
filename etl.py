import json
import os
import urllib.request

path = "C:\\Users\\Thiago\\git\\google-mobility\\data"
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

filename = "sample.json"
os.path.join(path, filename)
with open(os.path.join(path, filename), 'w') as json_file:
    json.dump(json_list, json_file)