import requests
import pandas as pd
import json
import iso3166
import os

iso2_iso3 = iso3166.countries_by_alpha2

def updateGlobalData():
    url = "https://api.covid19api.com/summary"
    data = requests.get(url)
    data = json.loads(data.text)
    df_countries = pd.DataFrame(data["Countries"])
    df_countries["CountryCode"] = df_countries["CountryCode"].apply(lambda x:iso2_iso3[x].alpha3)
    global_data = data["Global"]
    df_countries.to_csv("data/countriesdata.csv")
    with open("data/globaldata.json", "w") as f:
        f.write(json.dumps(global_data))
    return (df_countries,global_data)

def getGlobalData():
    df_countries = pd.read_csv("data/countriesdata.csv")
    with open("data/globaldata.json", "r") as f:
        global_data = json.loads(f.read())
    return (df_countries,global_data)