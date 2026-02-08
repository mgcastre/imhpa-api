"""
Web scrapper to obtain hydromet data
M. G. Castrellon | February 2026
"""

# Load libraries
import requests
import pandas as pd

base_url = "https://www.imhpa.gob.pa/es/estaciones-satelitales"

los_naranjos = "estacion=114013&=108017&sensor=TEMP_PROM&ajax=1"

response = requests.get(base_url+"-data?estacion=114013&=108017&sensor=TEMP_PROM&ajax=1")

data_dict = response.json()

raw_records = data_dict.get('datos')
df = pd.DataFrame(raw_records, columns=['timestamp', 'value'])

df['date_time'] = pd.to_datetime(df['timestamp'], unit='ms')


df.loc[df['date_time'] >= "2026-01-30", :] \
    .plot(x='date_time', y='value')


