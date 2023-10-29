use Komenda

CREATE TABLE TempOsoba (
    pesel CHAR(11) PRIMARY KEY,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    data_urodzenia DATE,
    plec VARCHAR(20) CHECK (plec IN ('mezczyzna', 'kobieta'))
);

BULK INSERT TempOsoba FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv2\osoby.csv' 
WITH (
    FIELDTERMINATOR=',',
    FIRSTROW = 2
);

MERGE INTO Osoba AS target
USING TempOsoba AS source
ON (target.pesel = source.pesel)
WHEN MATCHED THEN
    UPDATE SET
        target.imie = source.imie,
        target.nazwisko = source.nazwisko,
        target.data_urodzenia = source.data_urodzenia,
        target.plec = source.plec
WHEN NOT MATCHED THEN
    INSERT (pesel, imie, nazwisko, data_urodzenia, plec)
    VALUES (source.pesel, source.imie, source.nazwisko, source.data_urodzenia, source.plec);

DROP TABLE TempOsoba;













select * from dbo.Osoba

BULK INSERT dbo.Funkcjonariusze FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv2\funkcjonariusze.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Funkcjonariusze


BULK INSERT dbo.Dyspozytorzy FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv2\dyspozytorzy.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Dyspozytorzy

BULK INSERT dbo.Zdarzenia FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv2\zdarzenia.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Zdarzenia

BULK INSERT dbo.UczestnicyZdarzenia FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv2\uczestnicy.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.UczestnicyZdarzenia

BULK INSERT dbo.Zgloszenia FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv2\zgloszenia.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Zgloszenia


BULK INSERT dbo.Interwencje FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv2\interwencje.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Interwencje

BULK INSERT dbo.Funkcjonariusze_Interwencje FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv2\funkcjonariusze_interwencje.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Funkcjonariusze_Interwencje

