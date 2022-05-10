# About

Dieses Repository beinhaltet den Code der Kampagne "Luftfilterbegehren" auf [luftfilterbegehren.at](https://luftfilterbegehren.at/).

# Setup

See below for dependencies.
- copy config/template.py to config/\_\_init\_\_.py
- fill in your database settings
- run ./run.py to start the local development server

# Dependencies

- python 3.10 (!)
- Flask 1.X https://flask.palletsprojects.com/en/1.1.x/
- SQLAlchemy https://docs.sqlalchemy.org/en/14/
- PyMySQL https://pymysql.readthedocs.io/en/latest/

# virtualenv

```bash
virtualenv -p python3 .
source bin/activate
pip install -r requirements.txt
```

# SMTP-Service

use the following to mock the smtp service for development:
```
docker run --rm -it -p 3000:80 -p 25:25 rnwood/smtp4dev
```

# Includes

- jQuery Core (C) jQuery Foundation, Inc. [MIT]
- Normalize.css (C) Nicolas Gallagher, Jonathan Neal [MIT]
- OpenSans (C) Steve Matteson [Apache]
- Oswald (C) Vernon Adams [OFL]
