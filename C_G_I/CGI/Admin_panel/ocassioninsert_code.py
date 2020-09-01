print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Me</title>'
print '</head>'
print '<body>'
import cgi, cgitb, config
frm=cgi.FieldStorage()
occ=frm.getvalue('occ')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO ocassion (oname)VALUES('%s')"%(occ)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print '''<script>
                    window.location='ocassioninsert.py?msg=Ocassion Inserted successfully'
                    </script>'''
except Exception as e:
    print e

print '</body>'
print '</html>'