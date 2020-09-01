print '''Content-type:text/html\r\n\r\n
<html>
<head>
<title>Success Login</title>
</head>
<body>'''
import cgi, config
frm=cgi.FieldStorage()
if frm.getvalue('ok'):
    email=frm.getvalue('email_id')
    pwd=frm.getvalue('pwd')
    cursor=config.db.cursor()
    cursor.execute("SELECT * FROM admin WHERE aemail_id='{}' AND apwd='{}'".format(email,pwd))
    result=cursor.fetchall()
    if result:
        print '''<script>
                    window.location='blank.py?msg=Login Successful'
                 </script>'''

print '''</body>
        </html>'''