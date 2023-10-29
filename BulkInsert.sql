use Komenda
delete from dbo.Dyspozytorzy
delete from dbo.Osoba
delete from dbo.Funkcjonariusze
delete from dbo.Funkcjonariusze_Interwencje
delete from dbo.Interwencje
delete from dbo.UczestnicyZdarzenia
delete from dbo.Zdarzenia
delete from dbo.Zgloszenia

select * from dbo.Dyspozytorzy
select * from dbo.Osoba
select * from dbo.Funkcjonariusze
select * from dbo.Funkcjonariusze_Interwencje
select * from dbo.Interwencje
select * from dbo.UczestnicyZdarzenia
select * from dbo.Zdarzenia
select * from dbo.Zgloszenia

BULK INSERT dbo.Osoba FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv\osoby.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Osoba

BULK INSERT dbo.Funkcjonariusze FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv\funkcjonariusze.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Funkcjonariusze


BULK INSERT dbo.Dyspozytorzy FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv\dyspozytorzy.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Dyspozytorzy

BULK INSERT dbo.Zdarzenia FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv\zdarzenia.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Zdarzenia

BULK INSERT dbo.UczestnicyZdarzenia FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv\uczestnicy.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.UczestnicyZdarzenia

BULK INSERT dbo.Zgloszenia FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv\zgloszenia.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Zgloszenia


BULK INSERT dbo.Interwencje FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv\interwencje.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Interwencje

BULK INSERT dbo.Funkcjonariusze_Interwencje FROM 'C:\Users\User\Documents\SQL Server Management Studio\HD\csv\funkcjonariusze_interwencje.csv' 
WITH (
	FIELDTERMINATOR=',',
	FIRSTROW = 2
)

select * from dbo.Funkcjonariusze_Interwencje

select * from Osoba where pesel='86925415719'