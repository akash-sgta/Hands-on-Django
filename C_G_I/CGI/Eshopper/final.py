import check_cookie,config,cgi,cgitb
cursor = config.db.cursor()
frm = cgi.FieldStorage()
name=frm.getvalue('uname')
address=frm.getvalue('uadd')
contact=frm.getvalue('uphone')
amount=frm.getvalue('total')
prodid=frm.getvalue('proid')

try:
    uid = check_cookie.lst[0]
    sql = "INSERT INTO orders ( uid, uname, uaddress, uphone, amount, pid)VALUES('{}','{}','{}','{}','{}','{}')".format(uid,name,address,contact,amount,prodid)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
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
        	</header><!--/header-->'''
        print '<center><img src=images/tick.jpg height="200" width="200"></center>'
        print '<h2 align="center"> Your Order Has Been Placed</h2><br><br>'
        print '<a href="index.py"><center><input type="button" value="Continue Shopping"></center></a>'
except Exception as e:
    print e