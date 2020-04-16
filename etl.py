import json
import os
import urllib.request
import pandas as pd 
path = "/data"

def json_to_table(dataset, name, st):
    """
    get the six features inside of the Json

    Output: dataset (pandas) with date and value for the feature
    """
    feature = []
    for state in dataset["state"][name]["points"]:
        date = state["date"]
        value = state["value"]
        feature.append([st, date, value])
    return pd.DataFrame(feature, columns=["ST", "date", "value"])


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",  "DE", "FL", "GA", 
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

retailAndRecreation = []
groceryAndPharmacy = []
parks = []
transitStations = []
workplaces = []
residential = []

for i in states:
    with urllib.request.urlopen("https://pastelsky.github.io/covid-19-mobility-tracker/output/US/" + i + "/mobility.json") as url:
        data = json.loads(url.read().decode())
    retailAndRecreation.append(json_to_table(data, "retailAndRecreation",i))
    groceryAndPharmacy.append(json_to_table(data, "groceryAndPharmacy",i))
    parks.append(json_to_table(data, "parks",i))
    transitStations.append(json_to_table(data, "transitStations",i))
    workplaces.append(json_to_table(data, "workplaces",i))
    residential.append(json_to_table(data, "residential",i))
    
#concat data
retailAndRecreation = pd.concat(retailAndRecreation)
groceryAndPharmacy = pd.concat(groceryAndPharmacy)
parks = pd.concat(parks)
transitStations = pd.concat(transitStations)
workplaces = pd.concat(workplaces)
residential = pd.concat(residential)

#Save dataset
retailAndRecreation.to_csv( os.path.join(path, "retailAndRecreation.csv"), index= False)
groceryAndPharmacy.to_csv( os.path.join(path, "groceryAndPharmacy.csv"), index= False)
parks.to_csv( os.path.join(path, "parks.csv"), index= False)
transitStations.to_csv( os.path.join(path, "transitStations.csv"), index= False)
workplaces.to_csv( os.path.join(path, "workplaces.csv" ), index= False)
residential.to_csv( os.path.join(path, "residential.csv"), index= False)

