import check_cookie

import cgi,cgitb,config
cursor = config.db.cursor()

frm=cgi.FieldStorage()
prodid=frm.getvalue('pid')

cursor.execute("SELECT * FROM product WHERE pid='{}' ".format(prodid))
prod = cursor.fetchall()
quan=1
for rec in prod:
    price=rec[4]
    pname=rec[1]
    fpath=rec[7]

try:
    uid = check_cookie.lst[0]
    cursor=config.db.cursor()
    sql = "INSERT INTO cart ( uid, pid, quantity, price, pname, fpath)VALUES('{}','{}','{}','{}','{}','{}')".format(uid, prodid,quan, price,pname,fpath)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print """
            <html>
                <body>
                <script>
                window.location='index.py?msg=added to cart'
                </script>
                </body>
            </html>"""
except Exception as e:
    #print e
    print """
                <html>
                    <body>
                    <script>
                    window.location='login.py?msg=Login yourself'
                    </script>
                    </body>
                </html>"""
