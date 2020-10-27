
-- -----districts-----

CREATE TABLE districts(
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY(id)
);

-- -----states-----

CREATE TABLE states(
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  capital_id INT,
  PRIMARY KEY(id),
  FOREIGN KEY(capital_id) REFERENCES districts(id) ON DELETE SET NULL
);

-- -----users-----

CREATE TABLE users(
  id INT NOT NULL AUTO_INCREMENT,
  f_name VARCHAR(127) NOT NULL,
  l_name VARCHAR(127),
  email VARCHAR(255) NOT NULL,
  pass VARCHAR(31) NOT NULL,
  address VARCHAR(511) NOT NULL,
  state_id INT,
  district_id INT,
  pincode INT(7),
  phone VARCHAR(15),
  PRIMARY KEY(id),
  FOREIGN KEY(state_id) REFERENCES states(id) ON DELETE SET NULL,
  FOREIGN KEY(district_id) REFERENCES districts(id) ON DELETE SET NULL
);

-- -----admins-----

CREATE TABLE admins(
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  pass VARCHAR(63) NOT NULL,
  token VARCHAR(255),
  PRIMARY KEY(id, user_id),
  FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- -----occations-----

CREATE TABLE occations(
    id INT NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY(id)
);

-- -----images-----

CREATE TABLE images(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(31),
    src_1 VARCHAR(511) NOT NULL,
    src_2 VARCHAR(511),
    src_3 VARCHAR(511),
    src_4 VARCHAR(511),
    src_5 VARCHAR(511),
    PRIMARY KEY(id)
);

-- -----products-----

CREATE TABLE products(
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  keyword_1 VARCHAR(32) NOT NULL,
  keyword_2 VARCHAR(32),
  details VARCHAR(2047) NOT NULL,
  price DECIMAL(7,2) NOT NULL,
  occation_id INT,
  brand varchar(255) NOT NULL,
  image_id INT,
  PRIMARY KEY(id),
  FOREIGN KEY(occation_id) REFERENCES occations(id) ON DELETE SET NULL,
  FOREIGN KEY(image_id) REFERENCES images(id) ON DELETE SET NULL
);

-- -----INSERT dummy-----

INSERT INTO districts(name)
VALUES
('dummy district one'),
('dummy district two'),
('dummy district three'),
('dummy district four'),
('dummy district five');

INSERT INTO states(name, capital_id)
VALUES
('dummy state one', 1),
('dummy state two', 5),
('dummy state three', 2),
('dummy state four', NULL),
('dummy state five', NULL);

INSERT INTO users(f_name, l_name, email, pass, address, state_id, district_id, pincode, phone)
VALUES
('Dummy_f_one', 'Dummy_l_one', 'Dummy_one@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 1, NULL, NULL, '9876543210'),
('Dummy_f_two', 'Dummy_l_two', 'Dummy_two@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 1, NULL, NULL, '9876543211'),
('Dummy_f_three', 'Dummy_l_three', 'Dummy_three@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 2, NULL, NULL, '9876543212'),
('Dummy_f_four', 'Dummy_l_four', 'Dummy_four@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 2, NULL, NULL, '9876543213'),
('Dummy_f_five', 'Dummy_l_five', 'Dummy_five@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 3, NULL, NULL, '9876543214'),
('Dummy_f_six', 'Dummy_l_six', 'Dummy_six@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 3, NULL, NULL, '9876543215'),
('Dummy_f_seven', 'Dummy_l_seven', 'Dummy_seven@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 4, NULL, NULL, '9876543215'),
('Dummy_f_eight', 'Dummy_l_eight', 'Dummy_eight@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 4, NULL, NULL, '9876543216'),
('Dummy_f_nine', 'Dummy_l_nine', 'Dummy_nine@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 5, NULL, NULL, '9876543217'),
('Dummy_f_ten', 'Dummy_l_ten', 'Dummy_ten@gifthub.com', '1234', 'Dummy Address 1 2 3 4 5', 5, NULL, NULL, '9876543218');

INSERT INTO admins(user_id, pass)
VALUES
(1, '4321'),
(3, '4321');

INSERT INTO occations(name)
VALUES
('Dummy_occation_1'),
('Dummy_occation_2'),
('Dummy_occation_3'),
('Dummy_occation_4'),
('Dummy_occation_5');

