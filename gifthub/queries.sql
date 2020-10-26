CREATE TABLE admin (
  id int(11) NOT NULL,
  name varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  pass varchar(255) NOT NULL,
);

ALTER TABLE admin
ADD PRIMARY KEY(id) AUTO INCREMENT;