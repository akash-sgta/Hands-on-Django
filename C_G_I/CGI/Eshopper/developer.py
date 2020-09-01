print '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Developers</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">
    <link rel="stylesheet" type="text/css" href="swiper.min.css">
    <link rel="stylesheet" type="text/css" href="style1.css">

</head>
<body>

    <div class="swiper-container">
    <div class="swiper-wrapper">
        <div class="swiper-slide">
            <div class="imgBx">
                <img src="images\sanyam.jpg" height="300" width="300">
            </div>
            <div class="details">
                <h3>Sanyam Shaw<br><span>Web Developer</span></h3>
            </div>
        </div>
        <div class="swiper-slide">
            <div class="imgBx">
                <img src="images\priyam.jpg" height="300" width="300">
            </div>
            <div class="details">
                <h3>Priyam Das<br><span>Web Designer</span></h3>
            </div>
        </div>
        <div class="swiper-slide">
            <div class="imgBx">
                <img src="images\souriya.jpg" height="300" width="300">
            </div>
            <div class="details">
                <h3>Souriya Roy<br><span>Web Developer</span></h3>
            </div>
        </div>
        <div class="swiper-slide">
            <div class="imgBx">
                <img src="images\somnath.jpg" height="300" width="300">
            </div>
            <div class="details">
                <h3>Somnath Halder<br><span>Web Developer</span></h3>
            </div>
        </div>


    </div>
    <!-- Add Pagination -->
    <div class="swiper-pagination"></div>
  </div>
    <script type="text/javascript" src="swiper.min.js"></script>
    <script>
    var swiper = new Swiper('.swiper-container', {
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: 'auto',
      coverflowEffect: {
        rotate: 60,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows : true,
      },
      pagination: {
        el: '.swiper-pagination',
      },
    });
  </script>
</body>
</html>
    '''