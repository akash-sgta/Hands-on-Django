print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Me</title>'
print '</head>'
print '<body>'
import cgi, cgitb, config
frm=cgi.FieldStorage()
name=frm.getvalue('name')
address=frm.getvalue('address')
contact=frm.getvalue('contact')
email_id=frm.getvalue('email_id')
pwd=frm.getvalue('pwd')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO user (uname,uemail_id,upwd,uaddress,uphone)VALUES('%s','%s','%s','%s','%s')"%(name,email_id,pwd,address,contact)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print """
                        <html>
                            <body>
                            <script>
                            window.location='index.py?msg=Welcome'
                            </script>
                            </body>
                        </html>"""
except Exception as e:
    print e
print '</body>'
print '</html>'