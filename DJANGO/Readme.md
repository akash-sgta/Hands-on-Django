# CGI Shopping web application
## Authors : 
### Souriya Roy, github_link :
### Sanyam Shaw, github_link :
### Priyam, github_link :
### Somnath, github_link :


# Migrated to Django framework based web application
## Authors : (same as the preceding project "old")
## Migrated by : 
### Akash Sengupta, github_link : https://github.com/akash-sgta

### Steps:

pip install wheel\
pip install django\
pip install pillow\
pip install requests


python3 manage.py makemigrations main\
python3 manage.py makemigrations product\
python3 manage.py makemigrations admins\
python3 manage.py makemigrations user\
python3 manage.py makemigrations cart\
python3 manage.py makemigrations api

python3 manage.py migrate

