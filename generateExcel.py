import csv
import math
import uuid
import random
from datetime import datetime, timedelta
from copy import copy
import pandas as pd

education_levels = [
        'zasadnicze zawodowe',
        'zasadnicze branżowe',
        'średnie branżowe',
        'średnie',
        'wyższe'
    ]
desired_columns = [
        'id_funckjonariuszy',
        'imie',
        'nazwisko',
        'pesel',
        'data urodzenia',
        'wyksztalcenie',
        'ranga',
        'data zaczecia sluzby',
        'data zakonczenia sluzby'
    ]

def generateExcel():
    osoby_df = pd.read_csv('dane/osoby.csv')
    funkcjonariusze_df = pd.read_csv('dane/funkcjonariusze.csv')

    # Get 'osoby' where 'pesel' is in 'funkcjonariusze' 'pesel'
    result = pd.merge(funkcjonariusze_df,osoby_df, on='pesel')
    start_date = datetime(2019,1,1)  #yyyy mm dd
    result['data urodzenia'] = pd.to_datetime(result['data urodzenia'])
    max_date = result['data urodzenia'] + pd.DateOffset(years=18)
    result['data zaczecia sluzby'] = max_date + pd.to_timedelta((start_date - max_date).dt.days * random.random(), unit='D')
    result['data zaczecia sluzby'] = result['data zaczecia sluzby'].dt.strftime('%Y-%m-%d')
    result['data zakonczenia sluzby'] = ''
    komendant=1
    starszy_komisarz=math.floor(0.15*len(result))
    komisarz=math.floor(0.25*len(result))
    starszy_aspirant=math.floor(0.4*len(result))
    aspirant=len(result)-komisarz-starszy_aspirant-starszy_komisarz-komendant

    ranks = ['komendant'] * komendant + ['starszy_komisarz'] * starszy_komisarz + ['komisarz'] * komisarz + [
        'starszy_aspirant'] * starszy_aspirant + ['aspirant'] * aspirant

    random.shuffle(ranks)
    result['ranga'] = ranks

    result['wyksztalcenie'] = [random.choice(education_levels) for _ in range(len(result))]

    # result['data zaczecia sluzby']=['data urodzenia'] + pd.to_timedelta((start_date - result['data urodzenia']).max(),unit='D') * random.random()


    result = result[desired_columns]
    result.to_csv('daneExcel/excelDane1.csv', index=False)

def generateExcel2():
    osoby_df = pd.read_csv('dane2/osoby.csv')
    funkcjonariusze_df = pd.read_csv('dane2/funkcjonariusze.csv')
    excel=pd.read_csv('daneExcel/excelDane1.csv')
    rangi=['starzy komisarz','komisarz','starszy aspirant','aspirant']


    # Get 'osoby' where 'pesel' is in 'funkcjonariusze' 'pesel'
    result = pd.merge(funkcjonariusze_df,osoby_df, on='pesel')
    # print(result)
    start_date = datetime(2019, 1, 1)
    end_date=datetime(2020, 12, 31)#yyyy mm dd
    result['data zaczecia sluzby'] = result.apply(lambda row: generate_random_date(), axis=1)
    result['data zaczecia sluzby'] = result['data zaczecia sluzby'].dt.strftime('%Y-%m-%d')
    result['data zakonczenia sluzby'] = ''

    komisarz=math.floor(0.05*len(result))
    starszy_aspirant=math.floor(0.10*len(result))
    aspirant=len(result)-komisarz-starszy_aspirant

    ranks = ['komisarz'] * komisarz + ['starszy_aspirant'] * starszy_aspirant + ['aspirant'] * aspirant

    random.shuffle(ranks)
    result['ranga'] = ranks
    print(result['ranga'].value_counts())

    result['wyksztalcenie'] = [random.choice(education_levels) for _ in range(len(result))]
    result = result[desired_columns]
    # merged_result=pd.concat([excel,result],axis=0)
    merged_df = excel.set_index('pesel').combine_first(result.set_index('pesel')).reset_index()

    merged_result = result[desired_columns]
    merged_result.to_csv('daneExcel/excelDane2.csv', index=False)

def generate_random_date():
    start_date = datetime(2019, 1, 1)
    end_date = datetime(2020, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    return start_date + timedelta(days=random_days)


if __name__ == "__main__":
    generateExcel()
    generateExcel2()
