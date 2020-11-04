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


python3 manage.py makimigrations main\
python3 manage.py makimigrations product\
python3 manage.py makimigrations admins\
python3 manage.py makimigrations user\
python3 manage.py makimigrations cart

python3 manage.py migrate

