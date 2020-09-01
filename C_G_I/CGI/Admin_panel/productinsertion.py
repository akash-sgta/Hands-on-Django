

import cgi,config,cgitb
frm=cgi.FieldStorage()
print '''
<h2>Product Insertion Panel</h2>

<form name="frm" method="post" action="productinsert_code.py" enctype="multipart/form-data">
<div class="from-group">
    <label for="pname">Product Name</label>
    <input type="text" name="pname" class="form-control">
</div>

<div class="from-group">
    <label for="pkey">Product Keyword</label>
    <input type="text" name="pkey" class="form-control">
</div>

<div class="from-group">
    <label for="pdetails">Product Details</label>
    <input type="text" name="pdet" class="form-control">
</div>

<div class="from-group">
    <label for="pprice">Product Price</label>
    <input type="text" name="pprice" class="form-control">
</div>

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
</div>

<div class="from-group">
    <label for="pbrand">Product Brand</label>
    <input type="text" name="pbrand" class="form-control">
</div>

<div class="from-group">
	<label for="pimg">Product Image</label>
    <input type="file" name="file" class="">
</div>

<br>
	<input type="submit" name="ok" value="Insert" class="btn btn-primary">

</form>'''



