print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>'''
import cgi, config
form=cgi.FieldStorage()
pid=form.getvalue('id')

pname = form.getvalue('pname')
pprice=form.getvalue('pprice')
pkey=form.getvalue('pkey')
pdet=form.getvalue('pdet')
pbrand=form.getvalue('pbrand')
oid=form.getvalue('occ_id')
cursor = config.db.cursor()
sql = "UPDATE product SET pname='{}',pprice={},pkeyword='{}',pdetails='{}',pbrand='{}',oid={} WHERE pid={}".format(pname,pprice,pkey,pdet,pbrand,oid,pid)
if cursor.execute(sql):
    config.db.commit()
    config.db.close()
    print '''<script>
                window.location='updateprod.py?id={}&msg=Updated successfully'
            </script>'''.format(pid)

print '''</body>
</html>'''