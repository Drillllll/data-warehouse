import csv
import uuid
import random
from datetime import datetime, timedelta

input_file = "baby-names.csv"

min_id_funkcjonariusza = 10
max_id_funkcjonariusza = 10

min_ = 12

def generate_pesel():
    return str(random.randint(0, 99999999999)).zfill(11)

# generate osoby
def generate_person(N):
    names_with_sex = []
    with open('names.txt', 'r') as file:
        for line in file:
            name, sex = line.strip().split(',')
            names_with_sex.append((name, sex))
    with open('surnames.txt', 'r') as file:
        surnames = [line.strip() for line in file]

    pesel = random.sample(range(10**10, 10**11), N)
    name_sex = random.choice(names_with_sex)
    name = name_sex[0]
    plec = name_sex[1]
    start_date = datetime(1960, 1, 1)
    end_date = datetime(2002, 12, 31)

    # Calculate the number of days between start and end
    total_days = (end_date - start_date).days

    # Generate a random number of days between 0 and total_days
    random_days = random.randint(0, total_days)

    # Calculate the random date by adding random_days to the start_date
    random_date = start_date + timedelta(days=random_days)
    print("Random Date:", random_date.strftime("%Y-%m-%d"))
    print(pesel)

if __name__ == "__main__":
    print("hello world")
    generate_person(12  )

