import csv
import uuid
import random
from datetime import datetime, timedelta
from copy import copy

F = 20
Fmin = 1
D = 10
Dmin = 1
U = 200
Umin = 1
Z = 100
Zmin = 1
I = 110
Imin = 1
folderPath = 'dane/'


# generuje dane dla zbioru encji Osoby w csv
# zwraca tablice peseli
def generate_osoby(N):
    names_with_sex = []
    with open('input/names.txt', 'r') as file:
        for line in file:
            name, sex = line.strip().split(',')
            names_with_sex.append((name, sex))
    with open('input/surnames.txt', 'r') as file:
        surnames = [line.strip() for line in file]

    pesel = random.sample(range(10 ** 10, 10 ** 11), N)
    name_sex = random.sample(names_with_sex, N)
    names, sex = zip(*name_sex)

    start_date = datetime(1960, 1, 1)
    end_date = datetime(2002, 12, 31)
    birth = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(N)]
    birth_strings = [date.strftime('%Y-%m-%d') for date in birth]

    data = list(zip(pesel, names, surnames, birth_strings, sex))
    # Open the CSV file for writing
    with open(folderPath + 'osoby.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(['pesel', 'imie', 'nazwisko', 'data urodzenia', 'plec'])  # Write header
        writer.writerows(data)
    return pesel


# generuje csv dla funckjonariuszy i zwraca tablice id ufnkcjinariuszy i zaktualizowane pesele
def generate_funkjonariusze(F, Fmin, pesele):
    id_funckjonariuszy = []
    for i in range(Fmin, Fmin + F + 1):
        id_funckjonariuszy.append(i)
    pesel_funkcjonariusze = pesele[:F]
    left_pesels = pesele[F:]

    data = list(zip(id_funckjonariuszy, pesel_funkcjonariusze))
    with open(folderPath + 'funkcjonariusze.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(['id_funckjonariuszy', 'pesel'])  # Write header
        writer.writerows(data)
    return id_funckjonariuszy, left_pesels


def generate_dyspozytorzy(D, Dmin, pesele):
    numery_dyspozytorow = []
    for i in range(Dmin, Dmin + D + 1):
        numery_dyspozytorow.append(i)
    pesel_dyspozytorzy = pesele[:D]
    left_pesels = pesele[D:]
    data = list(zip(numery_dyspozytorow, pesel_dyspozytorzy))
    with open(folderPath + 'dyspozytorzy.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(['numer dyspozytora', 'pesel'])  # Write header
        writer.writerows(data)
    return numery_dyspozytorow, left_pesels


def generate_uczestnicy(U, Umin, pesele, id_zdarzenia, Z):


    id_uczestnicy = []
    for i in range(Umin, Umin + U + 1):
        id_uczestnicy.append(i)
    pesel_uczestnicy = pesele[:U]
    left_pesels = pesele[U:]

    wybrane_zdarzenia = []
    for j in range(Z):
        wybrane_zdarzenia.append(id_zdarzenia[j])
    for k in range(Z, U):
        wybrane_zdarzenia.append(random.choice(id_zdarzenia))



    data = list(zip(id_uczestnicy, pesel_uczestnicy, wybrane_zdarzenia))
    with open(folderPath + 'uczestnicy.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(['id uczestnika', 'pesel', 'id_zdarzenia'])  # Write header
        writer.writerows(data)
    return id_uczestnicy, left_pesels


def generate_zdarzenia(Z, Zmin):
    id_zdarzenia = []
    for i in range(Zmin, Zmin + Z + 1):
        id_zdarzenia.append(i)

    # adres
    with open('input/ulice.txt', 'r') as file:
        lines = file.readlines()
    ulice = random.sample(lines, Z)
    adresy = [f"{line.strip()} {random.randint(1, 50)}" for line in ulice]

    # godzina
    godziny_zdarzen_string = []
    for _ in range(Z):
        godzina = random.randint(0, 23)
        minuty = random.randint(0, 59)
        sekundy = random.randint(0, 59)
        losowa_godzina = str(godzina) + ':' + str(minuty) + ':' + str(sekundy)
        godziny_zdarzen_string.append(losowa_godzina)

    # data
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2023, 12, 31)
    daty_zdarzen = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(Z)]
    daty_zdarzen_string = [d.strftime('%Y-%m-%d') for d in daty_zdarzen]


    data = list(zip(id_zdarzenia, adresy, godziny_zdarzen_string, daty_zdarzen_string))
    with open(folderPath + 'zdarzenia.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(['id_zdarzenia', 'adres', 'godzina', 'data'])  # Write header
        writer.writerows(data)

    return id_zdarzenia, godziny_zdarzen_string


def generate_zgloszenia(Z, Zmin, id_zdarzen, numery_dyspozytorow, godziny_zdarzen):
    id_zgloszenia = []
    for i in range(Zmin, Zmin + Z + 1):
        id_zgloszenia.append(i)

    godziny_pozniejsze = []
    # Ile godzin dodac
    for godzina_string in godziny_zdarzen:
        godzina = datetime.strptime(godzina_string, "%H:%M:%S")
        losowa_liczba_minut = random.randint(1, 5)
        pozniejsza_godzina = godzina + timedelta(minutes=losowa_liczba_minut)
        godziny_pozniejsze.append(pozniejsza_godzina.strftime("%H:%M:%S"))

    pilnosci = []
    for _ in range(Z):
        pilnosci.append(random.randint(1, 5))

    rodzaje_csv = []
    mozliwe_rodzaje = ["drogowe", "kryminalne", "inne"]
    for _ in range(Z):
        losowy_string = random.choice(mozliwe_rodzaje)
        rodzaje_csv.append(losowy_string)

    numery_dyspozytorow_do_zgloszen = []
    for _ in range(Z):
        numery_dyspozytorow_do_zgloszen.append(random.choice(numery_dyspozytorow))

    id_zdarzen_do_zgloszen = []
    for i in range(Z):
        id_zdarzen_do_zgloszen.append(id_zdarzen[i])

    data = list(zip(id_zdarzen, godziny_pozniejsze, pilnosci, rodzaje_csv, numery_dyspozytorow_do_zgloszen,id_zdarzen_do_zgloszen))
    with open(folderPath + 'zgloszenia.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(['id_zgloszenia',  'godzina','pilnosci', 'rodzja', 'numer dyspozytora','id_zdarzenia'])  # Write header
        writer.writerows(data)
    return id_zgloszenia, godziny_pozniejsze

def generate_interwencje(I, Z, Imin, id_zgloszen, godziny_zgloszen):
    id_interwencji = []
    for i in range(Imin, Imin + I + 1):
        id_interwencji.append(i)

    dlugosc_interwencji_string = []
    for _ in range(I):
        godzina = random.randint(0, 1)
        minuty = random.randint(0, 30)
        sekundy = random.randint(0, 59)
        losowa_godzina = str(godzina) + ':' + str(minuty) + ':' + str(sekundy)
        dlugosc_interwencji_string.append(losowa_godzina)

    id_zgloszen_csv = []
    for i in range(Z):
        id_zgloszen_csv.append(id_zgloszen[i])
    for j in range(I-Z): #lecimy od poczatku
        id_zgloszen_csv.append(id_zgloszen[j])

    godziny_interwencji = []

    for k in range(Z):
        godzina = datetime.strptime(godziny_zgloszen[k], "%H:%M:%S")
        losowa_liczba_minut = random.randint(5, 15)
        pozniejsza_godzina = godzina + timedelta( minutes=losowa_liczba_minut)
        godziny_interwencji.append(pozniejsza_godzina.strftime("%H:%M:%S"))
    for l in range(I-Z):
        godzina = datetime.strptime(godziny_zgloszen[l], "%H:%M:%S")
        losowa_liczba_minut = random.randint(5, 15)
        pozniejsza_godzina = godzina + timedelta( minutes=losowa_liczba_minut)
        godziny_interwencji.append(pozniejsza_godzina.strftime("%H:%M:%S"))

    data = list(zip(id_interwencji, godziny_interwencji, dlugosc_interwencji_string, id_zgloszen_csv))
    with open(folderPath + 'interwencje.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(['id_interwencji', 'godziny_interwencji', 'dlugosc_interwencji', 'id_zgloszen'])  # Write header
        writer.writerows(data)

    return id_interwencji


def generate_funkcjonarjusze_interwencje(id_interwencji, I, id_funkcjonarjuszy):
    wybrani_funkcjonariusze = []
    for i in range(I):
        wybrani_funkcjonariusze.append(random.choice(id_funkcjonarjuszy))
    pass

    data = list(zip(wybrani_funkcjonariusze, id_interwencji))
    with open(folderPath + 'funkcjonariusze_interwencje.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(['id_funkcjonariuszy', 'id_interwencji'])  # Write header
        writer.writerows(data)

if __name__ == "__main__":
    print("GENERATOR DANYCH V. 3.0.3 - MINDSET MILIONERA")
    print("kodowany in Gogi Case")
    pesele = generate_osoby(F + D + U)
    id_funckjonariuszy, pesele = generate_funkjonariusze(F, Fmin, pesele)
    numery_dyspozytorow, pesele = generate_dyspozytorzy(D, Dmin, pesele)


    id_zdarzen, godziny_zdarzen = generate_zdarzenia(Z, Zmin)

    id_uczestnikow, _ = generate_uczestnicy(U, Umin, pesele, id_zdarzen, Z)

    id_zgloszen, godziny_zgloszen = generate_zgloszenia(Z, Zmin, id_zdarzen, numery_dyspozytorow, godziny_zdarzen)
    id_interwencji = generate_interwencje(I, Z, Imin, id_zgloszen, godziny_zgloszen)
    generate_funkcjonarjusze_interwencje(id_interwencji, I, id_funckjonariuszy)


# TODO
# widzieliscie kiedys ciezarna lalke barbie
# nie bo ken dochodzi zawsze w drugim pudelku
# JAK KUPUJESZ BRON Z DARKNETA TO MONERO!!
# porady i żarty od Doktora Andrzeja Sobeckiego
