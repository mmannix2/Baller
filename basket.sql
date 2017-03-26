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

INSERT INTO players (phone, name, zipcode, zipRange, fun, intense, hardcore) VALUES ('5406661234', 'Johnny Basketball', 12345, 5, true, true, true);
INSERT INTO players (phone, name, zipcode, zipRange, fun, intense, hardcore) VALUES ('1234567890', 'Michael Jordan', 12340, 5, false, false, true);
INSERT INTO players (phone, name, zipcode, zipRange, fun, intense, hardcore) VALUES ('7031234792', 'Larry Bird', 12348, 5, true, false, true);

CREATE TABLE games (
	id serial NOT NULL PRIMARY KEY,
	address text NOT NULL,
	city text NOT NULL,
        state text NOT NULL,
	zip int NOT NULL,
	tipOff time NOT NULL,
	day date NOT NULL,
	fun boolean NOT NULL,
	intense boolean NOT NULL,
	hardcore boolean NOT NULL
);

INSERT INTO games (address, city, state, zip, tipOff, day, fun, intense, hardcore) VALUES ('742 Evergreen Terrace', 'Springfield', 'VA', 12345, '12:00 PM', 'Mar-28-2017', true, false, false);
INSERT INTO games (address, city, state, zip, tipOff, day, fun, intense, hardcore) VALUES ('500 Cherry Ave', 'Charlottesville', 'VA', 12345, '2:30 PM', 'Mar-30-2017', false, true, false);

CREATE TABLE registered(
	phone varchar(10) NOT NULL REFERENCES players(phone),
	gameID serial NOT NULL REFERENCES games(id)
);

INSERT INTO registered (phone, gameID) VALUES ('5406661234', 1);
INSERT INTO registered (phone, gameID) VALUES ('1234567890', 1);
