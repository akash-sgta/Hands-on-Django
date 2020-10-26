-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2020 at 01:41 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cgi_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `aid` int(11) NOT NULL,
  `aname` varchar(255) NOT NULL,
  `aemail_id` varchar(255) NOT NULL,
  `apwd` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`aid`, `aname`, `aemail_id`, `apwd`) VALUES
(1, 'Sanyam Shaw', 'sanyam@gmail.com', 'sanyam'),
(2, 'Priyam Das', 'priyam@gmail.com', 'priyam'),
(3, 'Souriya Roy', 'souriya@gmail.com', 'souriya'),
(4, 'Somnath Halder', 'somnath@gmail.com', 'somnath');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cartid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `pname` varchar(255) NOT NULL,
  `fpath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`cartid`, `uid`, `pid`, `quantity`, `price`, `pname`, `fpath`) VALUES
(41, 12, 4, 1, 599, 'Choco Gem Cake', 'uploaded_files/bimg1.jpg'),
(42, 12, 6, 1, 299, 'Singing Box', 'uploaded_files/bimg3.jpg'),
(43, 12, 10, 1, 999, 'Ferrero Rocher Rumballs', 'uploaded_files/bimg7.jpg'),
(44, 14, 4, 2, 599, 'Choco Gem Cake', 'uploaded_files/bimg1.jpg'),
(45, 14, 5, 1, 300, 'Happy Birthday Card', 'uploaded_files/bimg2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `ocassion`
--

CREATE TABLE `ocassion` (
  `oid` int(11) NOT NULL,
  `oname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ocassion`
--

INSERT INTO `ocassion` (`oid`, `oname`) VALUES
(1, 'Birthday'),
(2, 'Anniversary'),
(3, 'Wedding');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `odid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `uaddress` varchar(255) NOT NULL,
  `uphone` varchar(255) NOT NULL,
  `amount` int(11) NOT NULL,
  `pid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`odid`, `uid`, `uname`, `uaddress`, `uphone`, `amount`, `pid`) VALUES
(23, 12, 'Sanyam Shaw', 'Seals Garden', '9748303477', 1198, 4),
(24, 12, 'Sanyam Shaw', 'Seals Garden', '9748303477', 300, 5),
(25, 12, 'Sanyam Shaw', 'Seals Garden', '9748303477', 299, 6),
(26, 14, 'souriya', '23 E Suri Lane', '9051366313', 1198, 4),
(27, 14, 'souriya', '23 E Suri Lane', '9051366313', 300, 5);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `pid` int(11) NOT NULL,
  `pname` varchar(255) NOT NULL,
  `pkeyword` varchar(255) NOT NULL,
  `pdetails` varchar(255) NOT NULL,
  `pprice` int(11) NOT NULL,
  `oid` int(11) NOT NULL,
  `pbrand` varchar(255) NOT NULL,
  `fpath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`pid`, `pname`, `pkeyword`, `pdetails`, `pprice`, `oid`, `pbrand`, `fpath`) VALUES
(4, 'Choco Gem Cake', 'cake', 'Chocolate cake with gems filling ', 599, 1, 'Mio Amore', 'uploaded_files/bimg1.jpg'),
(5, 'Happy Birthday Card', 'card', 'Birthday card made from recycled paper', 300, 1, 'Archies', 'uploaded_files/bimg2.jpg'),
(6, 'Singing Box', 'toy', 'Singing box that can be personalized to any song you want', 299, 1, 'Archies', 'uploaded_files/bimg3.jpg'),
(7, 'Barbie Doll Set', 'toy', 'Barbie Set including the doll and its small household', 699, 1, 'Disney', 'uploaded_files/bimg4.jpg'),
(8, 'Hot Wheels Cars set', 'toy', 'Hot wheels set consisting of 10 metallic cars ', 1500, 1, 'Matel', 'uploaded_files/bimg5.jpeg'),
(9, 'Tricycle for Kids', 'cycle', 'Tricycle with a twist meant for kids under 6 years of age', 1499, 1, 'Shaw Cycles Ltd.', 'uploaded_files/bimg6.jpg'),
(10, 'Ferrero Rocher Rumballs', 'chocolate', 'Set of rumballs from a reputed brand', 999, 1, 'Rochers', 'uploaded_files/bimg7.jpg'),
(11, 'Bouquet for Birthdays', 'flowers', 'Colorful Bouquet comprised of different flowers', 799, 1, 'Happy Products', 'uploaded_files/bimg8.jpg'),
(12, 'Fragrance bottle Set', 'perfume', 'Set of 3 bottles of the popular fragrances.', 6999, 2, 'Chanel', 'uploaded_files/aimg1.jpg'),
(13, 'Wallet for Men', 'men', 'Wallet made from the finest leather imported from The United Kingdom', 1599, 2, 'Gubintu', 'uploaded_files/aimg2.jpg'),
(14, 'Purse for Women', 'women', 'Purse for women made from leather and decorated with pearls', 2599, 2, 'YYW', 'uploaded_files/aimg3.jpg'),
(15, 'Wooden Photo Frame ', 'frame', 'A wooden photo frame painted golden', 1399, 2, 'Archies', 'uploaded_files/aimg4.jfif'),
(16, 'Suit for Men', 'men', 'A two piece suit made from cotton with the tie included in the set', 4599, 2, 'Raymonds', 'uploaded_files/aimg5.jpg'),
(17, 'Long Dress for Women', 'women', 'A long dress for women with only one size available for now, i.e., 36.', 5999, 2, 'Louis Vuitton', 'uploaded_files/aimg6.jpg'),
(18, 'Gold Jewelry Set ', 'jewelry', 'A 24 carat gold set consisting of 7 pieces of different jewelry', 169999, 3, 'Senco Gold', 'uploaded_files/wimg1.jpg'),
(19, 'Wooden Wall Clock ', 'clock', 'Wooden wall clock which also shows the day of the week', 1999, 3, 'Rolex', 'uploaded_files/wimg2.jpeg'),
(20, 'Mixer Juicer Grinder', 'philips', 'Mixer Juicer Grinder made for daily use', 2499, 3, 'Philips', 'uploaded_files/wimg3.jfif'),
(21, '6\" x 7\" Bed', 'bed', 'A king sized bed made of wood', 13999, 3, 'Bodyworks', 'uploaded_files/wimg4.jpg'),
(22, 'White Almirah', 'storage', 'A white wooden almirah made for daily use', 4799, 3, 'Bodyworks', 'uploaded_files/wimg5.jpg'),
(23, 'Makeup Kit for women', 'women', 'A makeup kit comprised for several colors', 3599, 3, 'Chanel', 'uploaded_files/wimg6.jpg'),
(24, 'Grooming kit for Men', 'men', 'A grooming kit for men made from all natural materials', 3577, 3, 'Portland Mineral Store', 'uploaded_files/wimg7.jpg'),
(30, 'zdfff', 'dgdgdfdf', 'fdfafafsfa', 599, 3, 'sddddd', 'uploaded_files/wimg5.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `uid` int(11) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `uemail_id` varchar(255) NOT NULL,
  `upwd` varchar(255) NOT NULL,
  `uaddress` text NOT NULL,
  `uphone` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uid`, `uname`, `uemail_id`, `upwd`, `uaddress`, `uphone`) VALUES
(12, 'Sanyam Shaw', 'sanyam@gmail.com', 'sanyam', 'Seals Garden', '9748303477'),
(14, 'souriya', 'souriyaroy1998@gmail.com', 'tuttu', '23 E Suri Lane', '9051366313');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`aid`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cartid`);

--
-- Indexes for table `ocassion`
--
ALTER TABLE `ocassion`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`odid`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cartid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `ocassion`
--
ALTER TABLE `ocassion`
  MODIFY `oid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `odid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
