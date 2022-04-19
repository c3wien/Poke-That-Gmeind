#!/usr/bin/env python3
from json import load, dumps

with open('/tmp/gemeinden_JSON.json', "r") as f:
    cities = load(f)

objs = {}
for city in cities:
    gkz = (city["Gemeindekennziffer"])
    gemeindename = city["Gemeindename"]
    plz = city["PLZ"]
    www = city["Website"]
    mail = city["Mail"]
    obj = {
                "id": gkz,
                "name": {"name": gemeindename},
                "plz": plz,
                "contact": {
                    "mail": mail,
                    "www": www
                }
            }
    objs[gkz] = obj

with open('/tmp/wien_JSON.json', "r") as f:
    bezirke = load(f)

for plz in (bezirke["Bezirksname"].keys()):
    PLZ = str(plz)
    GKZ = "9"+PLZ[1:3]+"01"
    name = bezirke["Bezirksname"][plz]
    mail = bezirke["Mail"][plz]
    www = "https://www.wien.gv.at/bezirke/"+name.lower()+"/"
    obj = {
                "id": GKZ,
                "name": {"name": name},
                "plz": plz,
                "contact": {
                    "mail": mail,
                    "www": www
                }
          }
    objs[GKZ] = obj

print(dumps(objs))
