import cgi, config,check_cookie
frm=cgi.FieldStorage()
quan=frm.getvalue('quantity')
#print quan
pid=frm.getvalue('pid')
#print pid
try:
    uid = check_cookie.lst[0]
    cursor = config.db.cursor()
    sql = ("UPDATE cart SET quantity={} WHERE pid={} AND uid={} ".format(quan,pid,uid))
    print '''
                            <html>
                                <body>
                                <script>
                                window.location='order.py?pid={}' '''.format(pid)
    print'''                            </script>
                                </body>
                            </html>'''
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()

except Exception as e:
    print e