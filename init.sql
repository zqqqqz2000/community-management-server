CREATE DATABASE community CHARACTER SET UTF8;

USE community;

CREATE TABLE resident_information (
	id INTEGER NOT NULL AUTO_INCREMENT,
	username VARCHAR(32),
	password VARCHAR(128) NOT NULL,
	phone_number VARCHAR(20),
	name VARCHAR(10),
	job VARCHAR(64),
	PRIMARY KEY (id),
	UNIQUE (username)
)

CREATE TABLE property_management_information (
	id INTEGER NOT NULL AUTO_INCREMENT,
	username VARCHAR(32) NOT NULL,
	password VARCHAR(128) NOT NULL,
	PRIMARY KEY (id)
)

insert into property_management_information (username, password) values('admin', '21232f297a57a5a743894a0e4a801fc3');
