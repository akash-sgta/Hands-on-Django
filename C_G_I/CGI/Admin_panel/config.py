import MySQLdb
import sys
try:
    db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='cgi_project')
except Exception as e:
    print e