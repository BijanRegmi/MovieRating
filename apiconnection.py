import requests
import json

def movie_data(**kwargs):
    url = "http://www.omdbapi.com/?apikey=2899c678"
    
    options = {
        "title":"t",
        "year":"y",
        "plot":"plot",
        "category":"type"
    }
    kwargs["title"] = kwargs["title"].replace(" ","+")
    for key,param in options.items():
        val = kwargs.get(key, None)
        if val != None and val != "":
            url += "&" + param + "=" + val.lower()
    
    req = requests.get(url)
    data = json.loads(req.content)
    return data