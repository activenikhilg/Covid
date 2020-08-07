import requests
import pandas as pd
import json
import iso3166

iso2_iso3 = iso3166.countries_by_alpha2

def getGlobalData():
    url = "https://api.covid19api.com/summary"
    data = requests.get(url)
    data = json.loads(data.text)
    df_countries = pd.DataFrame(data["Countries"])
    df_countries["CountryCode"] = df_countries["CountryCode"].apply(lambda x:iso2_iso3[x].alpha3)
    global_data = data["Global"]
    return (df_countries,global_data)