


print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>Startmin - Bootstrap Admin Theme</title>

        <!-- Bootstrap Core CSS -->
        <link href="css/bootstrap.min.css" rel="stylesheet">

        <!-- MetisMenu CSS -->
        <link href="css/metisMenu.min.css" rel="stylesheet">

        <!-- Custom CSS -->
        <link href="css/startmin.css" rel="stylesheet">

        <!-- Custom Fonts -->
        <link href="css/font-awesome.min.css" rel="stylesheet" type="text/css">

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
</head>
<body>
<div id="wrapper">

            <!-- Navigation -->
            '''

import menu

print'''            <!-- Page Content -->
            <div id="page-wrapper">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-lg-12">
                            <h1 class="page-header">GIft Store Name</h1>
                        </div>
                        <div class="col-lg-6">
                        <h2>Update Panel</h2>
                        <br>
                        '''
import config,cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')
cursor=config.db.cursor()
cursor.execute('SELECT * FROM product WHERE pid={}'.format(id))
result=cursor.fetchall()
rec=result[0]

print'''
<form name="frm" method="post" action="updateprod_code.py">
<div class="from-group">
    <label for="pname">Product Name</label>
    <input type="text" name="pname" value="{}" class="form-control">
</div>'''.format(rec[1])

print'''
<div class="from-group">
    <label for="pkey">Product Keyword</label>
    <input type="text" name="pkey" value="{}" class="form-control">
</div>'''.format(rec[2])

print'''
<div class="from-group">
    <label for="pdetails">Product Details</label>
    <input type="text" name="pdet" value="{}" class="form-control">
</div>'''.format(rec[3])

print'''
<div class="from-group">
    <label for="pprice">Product Price</label>
    <input type="text" name="pprice" value="{}" class="form-control">
</div>'''.format(rec[4])

print'''
<div class="from-group">
    <label for="pbrand">Product Brand</label>
    <input type="text" name="pbrand" value="{}" class="form-control">
</div>'''.format(rec[6])

print'''
<div class="from-group">
    <label for="occassion">Occassion</label>
    <td colspan="2">
        <select name="occ_id" class="form-control">
            <option value="" selected>Select Category</option>'''
cursor=config.db.cursor()
cursor.execute('SELECT * FROM ocassion')
result=cursor.fetchall()
for rec in result:
    print '''<option value="{}">{}</option>'''.format(rec[0],rec[1])
print ''' </select>
    </td>
</div>'''

print'''
<br>
    <td><input type="hidden" name="id" value="{}"></td>
    <td><input type="submit" name="ok" value="Save Changes" class="btn btn-primary"></td>

</form>'''.format(id)


print'''
</div>

                        <!-- /.col-lg-12 -->
                    </div>
                    <!-- /.row -->
                </div>
                <!-- /.container-fluid -->
            </div>
            <!-- /#page-wrapper -->

        </div>

        <!-- /#wrapper -->

        <!-- jQuery -->
        <script src="js/jquery.min.js"></script>

        <!-- Bootstrap Core JavaScript -->
        <script src="js/bootstrap.min.js"></script>

        <!-- Metis Menu Plugin JavaScript -->
        <script src="js/metisMenu.min.js"></script>

        <!-- Custom Theme JavaScript -->
        <script src="js/startmin.js"></script>

    </body>
</html>'''


