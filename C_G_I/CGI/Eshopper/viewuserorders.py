import check_cookie
try:
    id = check_cookie.lst[0]
    #print id
    import cgi, cgitb, config
    cursor = config.db.cursor()
    cursor.execute('SELECT * FROM orders WHERE uid={}'.format(id))
    result = cursor.fetchall()
    print '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="">
            <meta name="author" content="">
            <title>My Orders</title>
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
        							<a href="index.py"><img src="images/img4.png" height="60" width="70" alt="" /></a>
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
        	<section id="cart_items">
        		<div class="container">
        			<div class="table-responsive cart_info">
        				<table class="table table-condensed">
        					<thead>
        						<tr class="cart_menu">
        							<td class="image">Item</td>
        							<td class="description">Description</td>
        							<td class="price">Price</td>
        							<td class="quantity">Status</td>
        						</tr>
        					</thead>'''
    for rec in result:
        item=rec[6]
        price=rec[5]
        #print item
        #print price
        cursor.execute('SELECT * FROM product WHERE pid={}'.format(item))
        res = cursor.fetchall()
        for req in res:
            img=req[7]
            name=req[1]
        print '''
        					<tbody>    
        						<tr>
        							<td class="cart_product">
        								<a href=""><img src="{}" height="100" width="75" alt=""></a>
        							</td>
        							<td class="cart_description">
        								<h4>{}</h4>
        								<p>Product ID: {}</p>
        							</td>
        							<td class="cart_price">
        								<p>INR {}</p>
        							</td>
        							<td>
        							    <p>ORDERED</p>
        							</td>
        						</tr>
        					</tbody>
        					</form>'''.format(img,name,item,price)
    print '''
        				</table>
        			</div>
        		</div>
        	</section> <!--/#cart_items-->
        	<footer id="footer"><!--Footer-->
        		<div class="footer-top">
        			<div class="container">
        				<div class="row">
        					<div class="col-sm-2">
        						<div class="companyinfo">
        							<h2><span>Gift</span>Hub</h2>
        							<p>The Joy of Gifting</p>
        						</div>
        					</div>
        				</div>
        			</div>
        		</div>

        		<div class="footer-widget">
        			<div class="container">
        				<div class="row">
        					<div class="col-sm-2">
        						<div class="single-widget">
        							<h2>Service</h2>
        							<ul class="nav nav-pills nav-stacked">
        								<li><a href="contact.py">Contact Us</a></li>
        							</ul>
        						</div>
        					</div>
        					<div class="col-sm-2">
        						<div class="single-widget">
        							<h2>Address</h2>
        							<ul class="nav nav-pills nav-stacked">
        								<li><a href="">Kolkata</a></li>
        							</ul>
        						</div>
        					</div>
        					<div class="col-sm-2">
        						<div class="single-widget">
        							<h2>About Shopper</h2>
        							<ul class="nav nav-pills nav-stacked">
        								<li><a href="">Company Information</a></li>
        								<li><a href="index.py">Shop for a item</a></li>
        								<li><a href="">Store Location</a></li>
        								<li><a href="">Affillate Program</a></li>
        								<li><a href="">Copyright</a></li>
        							</ul>
        						</div>
        					</div>
        				</div>
        			</div>
        		</div>

        		<div class="footer-bottom">
        			<div class="container">
        				<div class="row">
        					<p class="pull-left">Copyright 2013 E-SHOPPER Inc. All rights reserved.</p>
        				</div>
        			</div>
        		</div>

        	</footer><!--/Footer-->'''
except Exception as e:
    # print e
    print """
                        <html>
                            <body>
                            <script>
                            window.location='login.py?msg=Login yourself'
                            </script>
                            </body>
                        </html>"""
