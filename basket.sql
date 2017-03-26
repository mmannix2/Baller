\c postgres
DROP DATABASE IF EXISTS basket;
CREATE DATABASE basket;
\c basket

CREATE TABLE players (
	phone varchar(10) NOT NULL,
	name text NOT NULL,
	zipcode int NOT NULL,
	zipRange int NOT NULL,
	fun boolean NOT NULL,
	intense boolean NOT NULL,
	hardcore boolean NOT NULL,
	PRIMARY KEY (phone)
);

CREATE TABLE game (
	id serial NOT NULL PRIMARY KEY,
	address text NOT NULL,
	city text NOT NULL,
	zip int NOT NULL,
	tipOff time NOT NULL,
	day date NOT NULL,
	fun boolean NOT NULL,
	intense boolean NOT NULL,
	hardcore boolean NOT NULL
--PRIMARY KEY (id)
);

CREATE TABLE registered(
	phone varchar(10) NOT NULL REFERENCES players(phone),
	gameID serial NOT NULL REFERENCES game(id)
);
