from faker import Faker

import polars as pl
# import pandas as pd

import random


fake = Faker()

number_of_records = 1000000

first_names = [fake.first_name() for i in range(number_of_records)]
last_names = [fake.last_name() for i in range(number_of_records)]

ammatti_lista = ['yleislääkäri', 'sairaanhoitaja', 'kirurgi', 'anestesiahoitaja', 'anestesialääkäri', 'neurologi', 'onkologi']
ammatti = [random.choice(ammatti_lista) for i in range(number_of_records)]

osasto_id = list(range(1, 11))
osasto = [random.choice(osasto_id) for i in range(number_of_records)]

df = pl.DataFrame(
    {
        "first": first_names,
        "last": last_names,
        "ammatti": ammatti,
        "osasto_id": osasto,
    }
)

df.write_csv("people.csv")
print(df.head(5))

osasto_id = list(range(1, 11))

osasto_nimet = [
    'Sisätautiosasto',
    'Kirurginen osasto',
    'Päiväkirurginen osasto',
    'Lastenosasto',
    'Synnytysosasto',
    'Teho-osasto',
    'Kardiologinen osasto',
    'Neurologinen osasto',
    'Ortopedinen osasto',
    'Psykiatrinen osasto',
]

df_osastot = pl.DataFrame(
    {
        "osasto_id": osasto_id,
        "osaston_nimi": osasto_nimet,
    }
    )


df_osastot.write_csv("osastot.csv")
print(df_osastot.head(10))