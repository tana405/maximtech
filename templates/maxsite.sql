CREATE TABLE City
(
    Id INTEGER PRIMARY KEY,
    Name CHARACTER VARYING(30), NOT NULL
    Adress CHARACTER VARYING(60), NOT NULL
);

CREATE TABLE Excursion
(
    Id SERIAL PRIMARY KEY,
	CityId INTEGER REFERENCES City (Id), NOT NULL
    FIO CHARACTER VARYING(30), NOT NULL
    Adress CHARACTER VARYING(60), NOT NULL
	Phone CHARACTER VARYING(15), NOT NULL
	Class INTEGER, NOT NULL
	Count INTEGER, NOT NULL
	Data DATETIME, NOT NULL
);
