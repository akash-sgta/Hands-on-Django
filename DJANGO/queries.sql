CREATE TABLE admins(
  id INT(8) NOT NULL AUTO_INCREMENT,
  f_name VARCHAR(255) NOT NULL,
  l_name VARCHAR(255),
  email VARCHAR(255) NOT NULL,
  pass VARCHAR(255) NOT NULL,
  token VARCHAR(255),
  PRIMARY KEY(id)
);

I

CREATE TABLE users(
  id INT(15) NOT NULL AUTO_INCREMENT,
  f_name VARCHAR(255) NOT NULL,
  l_name VARCHAR(255),
  email VARCHAR(255) NOT NULL,
  pass VARCHAR(255) NOT NULL,
  address_1 VARCHAR(255) NOT NULL,
  address_2 VARCHAR(255),
  state_in VARCHAR(63) NOT NULL,
  district VARCHAR(127) NOT NULL,
  pincode INT(8) NOT NULL,
  phone INT(16),
  PRIMARY KEY(id)
);

CREATE TABLE occations(
    id INT(15) NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE images(
    id INT(31) NOT NULL AUTO_INCREMENT,
    src VARCHAR(256) NOT NULL,
    name VARCHAR(63),
    PRIMARY KEY(id)
);

CREATE TABLE products(
  id INT(15) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  keyword_1 VARCHAR(32) NOT NULL,
  keyword_2 VARCHAR(32),
  details VARCHAR(2047) NOT NULL,
  price DECIMAL(7,2) NOT NULL,
  occation_id INT(15) NOT NULL,
  brand varchar(255) NOT NULL,
  image_id INT(31) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(occation_id) REFERENCES occations(id),
  FOREIGN KEY(image_id) REFERENCES images(id)
);

CREATE TABLE states(
  id INT(15) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE districts(
  id INT(15) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE sndmap(
  state_id INT(15) NOT NULL,
  district_id INT(15) NOT NULL,
  PRIMARY KEY(state_id, district_id),
  FOREIGN KEY(state_id) REFERENCES states(id) ON DELETE CASCADE,
  FOREIGN KEY(district_id) REFERENCES districts(id) ON DELETE CASCADE
);