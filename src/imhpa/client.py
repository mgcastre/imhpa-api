"""
Client for the IMHPA API
M. G. Castrellon
February 2026
"""

import re
import json
import httpx
import pandas as pd
from bs4 import BeautifulSoup

class ImhpaClient:
    def __init__(self, timeout=10.0):
        self.client = httpx.Client(timeout=timeout)
        self.base_url = "https://www.imhpa.gob.pa/es"
        self.url_satellite = f"{self.base_url}/estaciones-satelitales"
    
    def get_sensors(self) -> dict:
        response = self.client.get(self.url_satellite)

        soup = BeautifulSoup(response.text, "lxml")
        script_tag = soup.find('script', string=re.compile(r'var sensores_satelital'))

        pattern = r'var sensores_satelital\s*=\s*(\{.*?\});'
        match = re.search(pattern, script_tag.string, re.DOTALL)

        if match:
            json_data = json.loads(match.group(1))
        
        return json_data

    def get_stations(self, sensor: str) -> pd.DataFrame:
        """
        Returns a dataframe with the stations available for a given sensor.
        """
        data_url = f"{self.url_satellite}-data2"
        response = self.client.get(data_url, params=dict(sensor=sensor))
        data = response.json()
        
        df = pd.DataFrame(data.get('estaciones'))
        df = df.T.reset_index().rename(columns={"index":"id"})

        for col in df.columns:
            df[col] = df[col].convert_dtypes()
        
        for col in ["latitud", "longitud"]:
            df[col] = df[col].astype(float)
        
        for col in ["id", "numero_estacion"]:
            df[col] = df[col].astype(int)

        return df

    def get_data(self, station_id: str, sensor: str) -> pd.DataFrame:
        url = f"{self.base_url}/estaciones-satelitales-data"
        params = {"estacion": station_id, "sensor": sensor, "ajax": "1"}
        
        response = self.client.get(url, params=params)
        data_dict = response.json()
        
        df = pd.DataFrame(data_dict['datos'], columns=['timestamp', 'value'])
        df['date_time'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.loc[:, ['date_time', 'value']]
        
        return df

    # def get_historical_met_stations(self, sensor: str):
    #     df = self._get_stations(data_type='clima-historicos', sensor=sensor)
    #     return df

    # def get_historical_averages(self, sensor: str, station_id: str):
    #     pass

