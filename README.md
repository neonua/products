Based on:
- python 2.7
- pgsql 9.4+

Are 2 settings files for production and developer:
settings/dev.py
settings/prod.py

When you try start project or use manage.py - add to end parameter '--settings' whit settings file needed.
Example for dev:
  --settings=prj.settings.dev 

########Deploy########
0) You can install components or use virtuarlenv.
1) Install components:
  
  pip install -r requirements.txt

if your pip PATH to python 3+, try it:
  pip2 or pip2.7

if permission denied - use superuser(root) permissions:

  sudo pip install -r requirements.txt

2) Connect your DB in settings/base.py

3) Makemigrations and migrate
  
  cd prj/
  python2.7 manage.py --settings=prj.settings.dev  makemigraions
  python2.7 manage.py --settings=prj.settings.dev  migrate

4) Create superuser
  
  cd prj/
  python2.7 manage.py --settings=prj.settings.dev  createsuperuser
  
5) Use fixtures

  cd prj && python2.7 manage.py --settings=prj.settings.dev loaddata --app=prj fixture.json
  
6) And Start project

  cd prj && python2.7 manage.py --settings=prj.settings.dev runserver
