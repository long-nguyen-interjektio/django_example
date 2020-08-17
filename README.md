# Django Example

version 1.10

python 2.7

### Installation

create virtualenv
```
sudo apt-get install python3-virtualenv   
virtualenv -p python2.7 venv
```

Enable venv
```
source venv/bin/activate
```

Install dependencies
```
[venv] pip install psycopg2
[venv] pip install Django==1.10 
[venv] python -m pip install pip-tools
[vene] pip-compile --output-file requirements.txt 
```

DB migration
```
python manage.py migrate
```

### Useful PostgresSQL cmd

```
sudo -u postgres createuser djangoexample 
sudo -u postgres createuser djangoexample WITH PASSWORD 'djangoexample'
sudo -u postgres createdb djangoexample -O djangoexample
```
