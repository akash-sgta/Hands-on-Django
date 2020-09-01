import cgi, cgitb, config

cursor = config.db.cursor()
frm=cgi.FieldStorage()
search=frm.getvalue('search')
cursor.execute('SELECT * FROM ocassion')
occ = cursor.fetchall()

cursor.execute("SELECT * FROM product WHERE pkeyword='{}' ".format(search))
prod = cursor.fetchall()
if prod:
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

    	<section id="slider"><!--slider-->
    		<div class="container">
    			<div class="row">
    				<div class="col-sm-12">
    					<div id="slider-carousel" class="carousel slide" data-ride="carousel">
    						<ol class="carousel-indicators">
    							<li data-target="#slider-carousel" data-slide-to="0" class="active"></li>
    							<li data-target="#slider-carousel" data-slide-to="1"></li>
    							<li data-target="#slider-carousel" data-slide-to="2"></li>
    						</ol>

    						<div class="carousel-inner">
    							<div class="item active">
    								<div class="col-sm-6">
    									<h1><span>E</span>-SHOPPER</h1>
    									<h2>Free E-Commerce Template</h2>
    									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
    								</div>
    								<div class="col-sm-6">
    									<img src="images/home/girl1.jpg" class="girl img-responsive" alt="" />
    									<img src="images/home/pricing.png"  class="pricing" alt="" />
    								</div>
    							</div>
    							<div class="item">
    								<div class="col-sm-6">
    									<h1><span>E</span>-SHOPPER</h1>
    									<h2>100% Responsive Design</h2>
    									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
    								</div>
    								<div class="col-sm-6">
    									<img src="images/home/girl2.jpg" class="girl img-responsive" alt="" />
    									<img src="images/home/pricing.png"  class="pricing" alt="" />
    								</div>
    							</div>

    							<div class="item">
    								<div class="col-sm-6">
    									<h1><span>E</span>-SHOPPER</h1>
    									<h2>Free Ecommerce Template</h2>
    									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
    								</div>
    								<div class="col-sm-6">
    									<img src="images/home/girl3.jpg" class="girl img-responsive" alt="" />
    									<img src="images/home/pricing.png" class="pricing" alt="" />
    								</div>
    							</div>

    						</div>

    						<a href="#slider-carousel" class="left control-carousel hidden-xs" data-slide="prev">
    							<i class="fa fa-angle-left"></i>
    						</a>
    						<a href="#slider-carousel" class="right control-carousel hidden-xs" data-slide="next">
    							<i class="fa fa-angle-right"></i>
    						</a>
    					</div>

    				</div>
    			</div>
    		</div>
    	</section><!--/slider-->

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
    							</div>'''.format(rec[0], rec[1])
    print'''    
    						</div><!--/category-products-->



    						<div class="shipping text-center"><!--shipping-->
    							<img src="images/img5.gif" height="350" width="330" alt="" />
    						</div><!--/shipping-->

    					</div>
    				</div>

    				<div class="col-sm-9 padding-right">
    					<div class="features_items"><!--features_items-->
    						<h2 class="title text-center">Products</h2><!--lop starts here-->'''
    for rec in prod:
        print'''
    						<div class="col-sm-4">
    							<div class="product-image-wrapper">
    								<div class="single-products">
    										<div class="productinfo text-center">
    											<img src="{}" width="300" height="250" alt="" />
    											<h2>Rs. {}</h2>
    											<p>{}</p><!--pass id-->
    											<a href="productdetails.py?pid={}" class="btn btn-default add-to-cart"><i class="fa fa-shopping-cart"></i>View Details</a>
    										</div>
    								</div>
    							</div>
    						</div>'''.format(rec[7], rec[4], rec[1], rec[0])
    print'''						
    					</div><!--features_items-->
    				</div>
    			</div>
    		</div>
    	</section>

    	'''
else:
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
        	<section id="slider"><!--slider-->
    		<div class="container">
    			<div class="row">
    				<div class="col-sm-12">
    					<div id="slider-carousel" class="carousel slide" data-ride="carousel">
    						<ol class="carousel-indicators">
    							<li data-target="#slider-carousel" data-slide-to="0" class="active"></li>
    							<li data-target="#slider-carousel" data-slide-to="1"></li>
    							<li data-target="#slider-carousel" data-slide-to="2"></li>
    						</ol>

    						<div class="carousel-inner">
    							<div class="item active">
    								<div class="col-sm-6">
    									<h1><span>E</span>-SHOPPER</h1>
    									<h2>Free E-Commerce Template</h2>
    									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
    								</div>
    								<div class="col-sm-6">
    									<img src="images/home/girl1.jpg" class="girl img-responsive" alt="" />
    									<img src="images/home/pricing.png"  class="pricing" alt="" />
    								</div>
    							</div>
    							<div class="item">
    								<div class="col-sm-6">
    									<h1><span>E</span>-SHOPPER</h1>
    									<h2>100% Responsive Design</h2>
    									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
    								</div>
    								<div class="col-sm-6">
    									<img src="images/home/girl2.jpg" class="girl img-responsive" alt="" />
    									<img src="images/home/pricing.png"  class="pricing" alt="" />
    								</div>
    							</div>

    							<div class="item">
    								<div class="col-sm-6">
    									<h1><span>E</span>-SHOPPER</h1>
    									<h2>Free Ecommerce Template</h2>
    									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
    								</div>
    								<div class="col-sm-6">
    									<img src="images/home/girl3.jpg" class="girl img-responsive" alt="" />
    									<img src="images/home/pricing.png" class="pricing" alt="" />
    								</div>
    							</div>

    						</div>

    						<a href="#slider-carousel" class="left control-carousel hidden-xs" data-slide="prev">
    							<i class="fa fa-angle-left"></i>
    						</a>
    						<a href="#slider-carousel" class="right control-carousel hidden-xs" data-slide="next">
    							<i class="fa fa-angle-right"></i>
    						</a>
    					</div>

    				</div>
    			</div>
    		</div>
    	</section><!--/slider-->

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
    							</div>'''.format(rec[0], rec[1])
    print'''    
    						</div><!--/category-products-->



    						<div class="shipping text-center"><!--shipping-->
    							<img src="images/img5.gif" height="350" width="330" alt="" />
    						</div><!--/shipping-->

    					</div>
    				</div>

    				<div class="col-sm-9 padding-right">
    					<div class="features_items"><!--features_items-->
    						<h2 class="title text-center">Products</h2><!--lop starts here-->'''
    for rec in prod:
        print'''
    						<div class="col-sm-4">
    							<div class="product-image-wrapper">
    								<div class="single-products">
    										<div class="productinfo text-center">
    											<img src="{}" width="300" height="250" alt="" />
    											<h2>Rs. {}</h2>
    											<p>{}</p><!--pass id-->
    											<a href="productdetails.py?pid={}" class="btn btn-default add-to-cart"><i class="fa fa-shopping-cart"></i>View Details</a>
    										</div>
    								</div>
    							</div>
    						</div>'''.format(rec[7], rec[4], rec[1], rec[0])
    print'''			<h4 >NO PRODUCTS AVAILABLE</h4>			
    					</div><!--features_items-->
    				</div>
    			</div>
    		</div>
    	</section>'''
