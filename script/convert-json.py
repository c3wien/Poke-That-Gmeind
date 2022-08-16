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
    if str(gkz)[0] == '9':
        gemeindename = "Wien " + gemeindename
        www = "https://www.wien.gv.at/stadtentwicklung/architektur/oeffentliche-bauten/"
        mail = "post@ma19.wien.gv.at"
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

print(dumps(objs))
