print '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h2>Products</h2>'''
import config,cgi
frm=cgi.FieldStorage()
if frm.getvalue('msg'):
    print frm.getvalue('msg')
cursor=config.db.cursor()
cursor.execute('SELECT * FROM product')
result=cursor.fetchall()
if result:
    print '''<table class="table table-striped table-bordered table-hover" id="dataTables-example">
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Details</th>
            <th>Price</th>
            <th>Brand</th>
            <th>Keyword</th>
            <th>Update</th>
        </tr>
    </thead>
    <tbody>'''
    for rec in result:
        print'''<tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>
                        <a href="updateprod.py?id={}"><img src="images/b_edit.png">
                        </a>
                    </td>
                </tr>'''.format(rec[0],rec[1],rec[3],rec[4],rec[6],rec[2],rec[0],rec[0])
    print'''</tbody>
    </table>
    '''
else:
    print 'No Products Found'