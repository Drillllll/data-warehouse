USE Komenda

CREATE TABLE Osoba (
	pesel CHAR(11) PRIMARY KEY,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    data_urodzenia DATE,
	plec VARCHAR(20) CHECK (plec IN ('mezczyzna', 'kobieta')),
	);

	
CREATE TABLE Dyspozytorzy (
	numerDyspozytora INTEGER primary key,
	pesel CHAR(11) REFERENCES Osoba
	);


CREATE TABLE Zdarzenia (
    idZdarzenia INTEGER PRIMARY KEY,
    adres VARCHAR(100),
    godzinaZdarzenia TIME,
    dataZdarzenia DATE
);

CREATE TABLE Zgloszenia (
    idZgloszenia INTEGER PRIMARY KEY,
    godzinaOdebrania TIME,
    pilnosc INT CHECK (pilnosc >= 1 AND pilnosc <= 5),
    rodzajZgloszenia VARCHAR(50) CHECK (RodzajZgloszenia IN ('drogowe', 'kryminalne', 'inne')),
	numerDyspozytora INTEGER REFERENCES Dyspozytorzy,
	idZdarzenia INTEGER REFERENCES Zdarzenia,
);


CREATE TABLE UczestnicyZdarzenia (
	idUczestnika INTEGER primary key,
	pesel CHAR(11) REFERENCES Osoba,
	idZdarzenia INTEGER REFERENCES Zdarzenia
	);


CREATE TABLE Interwencje (
    idInterwencji INTEGER PRIMARY KEY,
    godzinaDojazdu TIME,
    dlugoscInterwencji DATE,
	idZg³oszenia INTEGER REFERENCES Zgloszenia
);




Create Table Funkcjonariusze (
	idFunkcjonariusza INTEGER PRIMARY KEY,
	pesel CHAR(11) REFERENCES Osoba
);

Create Table Funkcjonariusze_Interwencje (
	idFunkcjonariusza INTEGER REFERENCES Funkcjonariusze,
	idInterwencji INTEGER REFERENCES Interwencje
);

