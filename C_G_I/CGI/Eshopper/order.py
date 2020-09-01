import check_cookie,config,cgi,cgitb
cursor = config.db.cursor()
frm = cgi.FieldStorage()

try:
    uid = check_cookie.lst[0]
    #print id
    pid = frm.getvalue('pid')
    cursor.execute('SELECT * FROM cart WHERE uid={} AND pid={} '.format(uid,pid))
    cart = cursor.fetchall()
    for rec in cart:
        quantity=rec[3]
        price=rec[4]
    total=price*quantity
    #print total
    cursor.execute('SELECT * FROM user WHERE uid={}'.format(uid))
    result = cursor.fetchall()
    print '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="">
            <meta name="author" content="">
            <title>Home | E-Shopper</title>
            <link href="css/bootstrap.min.css" rel="stylesheet">
            <link href="css/font-awesome.min.css" rel="stylesheet">
            <link href="css/prettyPhoto.css" rel="stylesheet">
            <link href="css/price-range.css" rel="stylesheet">
            <link href="css/animate.css" rel="stylesheet">
        	<link href="css/main.css" rel="stylesheet">
        	<link href="css/responsive.css" rel="stylesheet">
            <!--[if lt IE 9]>
            <script src="js/html5shiv.js"></script>
            <script src="js/respond.min.js"></script>
            <![endif]-->       
            <link rel="shortcut icon" href="images/ico/favicon.ico">
            <link rel="apple-touch-icon-precomposed" sizes="144x144" href="images/ico/apple-touch-icon-144-precomposed.png">
            <link rel="apple-touch-icon-precomposed" sizes="114x114" href="images/ico/apple-touch-icon-114-precomposed.png">
            <link rel="apple-touch-icon-precomposed" sizes="72x72" href="images/ico/apple-touch-icon-72-precomposed.png">
            <link rel="apple-touch-icon-precomposed" href="images/ico/apple-touch-icon-57-precomposed.png">
        </head><!--/head-->

        <body>
        	<header id="header"><!--header-->


        		<div class="header-middle"><!--header-middle-->
        			<div class="container">
        				<div class="row">
        					<div class="col-sm-4">
        						<div class="logo pull-left">
        							<a href="index.py"><img src="images/home/logo.png" alt="" /></a>
        						</div>

        					</div>
        					<div class="col-sm-8">
        						<div class="shop-menu pull-right">
        							<ul class="nav navbar-nav">
        							    <li><a href="login.py"><i class="fa fa-lock"></i> Login</a></li>
							            <li><a href="cart.py"><i class="fa fa-shopping-cart"></i> Cart</a></li>
								        <li><a href="logout.py"><i class="fa fa-user"></i> Logout</a></li>
        							</ul>
        						</div>
        					</div>
        				</div>
        			</div>
        		</div><!--/header-middle-->

        		<div class="header-bottom"><!--header-bottom-->
        			<div class="container">
        				<div class="row">
        					<div class="col-sm-9">
        						<div class="navbar-header">
        							<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        								<span class="sr-only">Toggle navigation</span>
        								<span class="icon-bar"></span>
        								<span class="icon-bar"></span>
        								<span class="icon-bar"></span>
        							</button>
        						</div>
        						<div class="mainmenu pull-left">
        							<ul class="nav navbar-nav collapse navbar-collapse">
        								<li><a href="index.py" class="active">Home</a></li>
								        <li><a href="about.py">About Us</a></li>
								        <li><a href="contact.py">Contact</a></li>
								        <li><a href="developer.py">Developers</a></li>
        							</ul>
        						</div>
        					</div>
        					<div class="col-sm-3">
        						<form name="form" method="post" action="search.py">
    						    <div class="search">
    						        <input type="text" name="search" placeholder="Search"/>
    							    <input type="submit" name="ok" value="Search">
    						    </div>
    						    </form>
        					</div>
        				</div>
        			</div>
        		</div><!--/header-bottom-->
        	</header><!--/header-->
        	<center>
        	<div class="shopper-informations">

					<div class="col-sm-3">
						<div class="shopper-info">
							<p>Shopper Information</p>'''
    for rec in result:
        print'''
								<form name="form" method="post" action="final.py?uid={}">
								NAME<input type="text" value="{}" name="uname" >
								ADDRESS<input type="text" value="{}" name="uadd" >
								CONTACT<input type="text" value="{}" name="uphone">
								TOTAL<input type="text" value="{}" name="total">
								PPRODUCT ID<input type="number" value="{}" name="proid">
								<input type="submit" name="ok" value="Confirm Order">
							</form>'''.format(uid,rec[1],rec[4],rec[5],total,pid)
    print'''
						</div>
					</div>
			</div>
        	</center>
        	</body>
        	</html>'''

except Exception as e:
    print e