print '''
 <!DOCTYPE html>
 <html lang="en">
 <head>
 	<meta charset="UTF-8">
 	<title>About Us</title>

 	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

 	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

 	<style>

		body{

			background: white;
			font-family:sans-serif;
			text-align: justify;
			overflow: hidden;

		}

		#about{
			padding-top: 98px;
			padding-bottom: 101px;
		}

		#about .triangle-right{
			margin-top: 95px;
			width: 0;
			height: 0;
			border-top: 259px solid transparent;
			border-left: 470px solid orange;
			border-bottom: 259px solid transparent;


		}

		#about .triangle-right img{
			position: absolute;
			left: -1px;
			top: 81px;
			width: 74%;

		}

		.fa-play{
			font-size: 100px;

		}


		#about .p-first{
			margin-bottom: 30px;
		}


		#about h2{
			margin-bottom: 47px;
			margin-top: 12px;

		}


		#about .social-link-text{
			margin-top: 50px;
			margin-bottom: 25px;

		}

		#about .about-link{
			padding-left: 0px;
		}

		#about .about-link li{
			display: inline-block;
		}

		#about .about-link li a i{
			width: 50px;
			height: 50px;
			border-radius: 50%;
			line-height: 50px;
			text-align: center;
			border: 1px solid #d6c6b2;
			margin-right: 10px;
			font-size: 22px;
			color: orange;
			transition: all .3s;

		}


		#about .about-link li a i:hover{
			color: #222222;
			background: orange;
			border-color: gray;

		}


		#about .about-img{
			position: relative;

		}

		#about .about-img{
			position: relative;

		}

		#about .about-img .man{
			position: absolute;
			bottom: 161px;
			top: 12px;
			left: -40px;
      width: 90%;
      height: 90%;
      padding: 40px;
      border-radius: 50%;
		}

		.color-3{
			color: darkgray;
		}


		.text-white{
			color: white;
		}


		p{
			margin-bottom: 0;
			font-size: 16px;
			line-height: 24px;
			color: #d6c6b2;
		}

		/*.btn-danger{
			border-radius: 0;
			padding: 10px 20px;
		}*/




	</style>


 </head>
 <body><br>
 <br>


 	<section id="about">

	<div class="container">
		<div class="row">
		<div class="col-md-5">
			<div class="about-img">
        <img  src="images/about_tringle.png">

            <img class="man" src="images/gift.jpg" alt="">

			</div>
		</div>
		<br>
		<div class="col-md-7 about-right">

			<h2 class="color-3" style="color: darkblue;"><b>About Us</b></h2>

			<p class="p-first text-white" style="color:black">
				At GiftHUB you will discover a gift bin for each event. Our excellent, top notch gifts are certain to awe even the most difficult to satisfy beneficiaries. Because of the assistance of our esteemed clients and item supply organizations, we have involvement in making flawlessly given gift containers filled the most awesome and novel things from around the globe. 
			</p>
			<p class="text-white" style="color:black">
				A tremendous measure of exertion goes into picking items to fill our India gifts bins to guarantee total consumer loyalty when each gift is gotten. Look over our wide choice of particular bins, including events, for example, Business Gifts, Corporate Gift Baskets, Easter, Fathers Day, Birthday, Get Well, Thank You and a lot more to locate your ideal gift for that unique individual. 
			</p>
			<br>
      <br>
      <br>
      <br>

			<ul class="about-link">
				<li><a href=""><i class="fa fa-fonticons" ></i></a></li>

				<li><a href=""><i class="fa fa-envira"></i></a></li>


				<li><a href=""><i class="fa fa-reddit-alien"></i></a></li>


				<li><a href=""><i class="fa fa-dribbble"></i></a></li>


				<li><a href=""><i class="fa fa-youtube-play"></i></a></li>

			</ul>


		</div>

		</div>
	</div>

 	</section>

 </body>
 </html>



'''