import check_cookie,config,cgi,cgitb
cursor = config.db.cursor()
frm = cgi.FieldStorage()
cid=frm.getvalue('pid')
pid=frm.getvalue('cid')
#print cid
#print pid
uid=check_cookie.lst[0]
#print uid
try:
    cursor = config.db.cursor()
    sql="DELETE FROM cart WHERE uid={} AND pid={} AND cartid={}".format(uid,pid,cid)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        #print 'deletion success'
        print '''<html>
        <body>
        <script>
        window.location='cart.py?msg=deletion success'
        </script>
        </body>
        </html>'''
except Exception as e:
    print e
