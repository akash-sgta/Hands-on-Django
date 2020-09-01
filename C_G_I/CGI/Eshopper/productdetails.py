import cgi,cgitb,config
cursor = config.db.cursor()

frm=cgi.FieldStorage()
id=frm.getvalue('pid')
cursor.execute('SELECT * FROM product WHERE pid={}'.format(id))
prod = cursor.fetchall()

cursor.execute('SELECT * FROM ocassion')
occ = cursor.fetchall()

print '''Content-type:text/html\r\n\r\n
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
	
<section>
		<div class="container">
			<div class="row">
			
				<div class="col-sm-3">
					<div class="left-sidebar">
						<h2>Category</h2>
						<div class="panel-group category-products" id="accordian"><!--category-productsr-->'''
for rec in occ:
    print'''
							<div class="panel panel-default">
								<div class="panel-heading">
									<h4 class="panel-title"><a href="occassionproduct.py?oid={}">{}</a></h4>
								</div>
							</div>'''.format(rec[0],rec[1])
print '''
						</div><!--/category-products-->
					</div>
				</div>'''
for rec in prod:
    print'''
				<div class="col-sm-9 padding-right">
					<div class="product-details"><!--product-details-->
						<div class="col-sm-5">
							<div class="view-product">
								<img src="{}" alt="" />								
							</div>
						</div>
						<div class="col-sm-7">
							<div class="product-information"><!--/product-information-->
								<img src="images/product-details/new.jpg" class="newarrival" alt="" />
								<h2>{}</h2>
								<p>Product ID: {}</p>
								<span>
									<span>INR {}</span>
									<button type="button" class="btn btn-fefault cart">
										<i class="fa fa-shopping-cart"></i>
										<a href="add_cart.py?pid={}">Add to cart</a>
									</button>
								</span>
								<p><b>Availability:</b> In Stock</p>
								<p><b>Description:</b> {}</p>
								<p><b>Brand:</b> {}</p>
							</div><!--/product-information-->
						</div>
					</div><!--/product-details-->
				</div>'''.format(rec[7],rec[1],rec[0],rec[4],rec[0],rec[3],rec[6])
print'''   
			</div>
		</div>
	</section>
</body>
</html>
'''