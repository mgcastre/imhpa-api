"""
Client for the IMHPA API
M. G. Castrellon
February 2026
"""

import httpx
import pandas as pd
from .constants import AVAILABLE_SENSORS

class ImhpaClient:
    def __init__(self, timeout=10.0):
        self.client = httpx.Client(timeout=timeout)
        self.base_url = "https://www.imhpa.gob.pa/es"
        self.sensors = AVAILABLE_SENSORS
    
    def list_sensors(self, data_type: str):
        """
        Returns a list of available sensors per data type:
        The user specifies either 'clima-historicos' or 'estaciones-satelitales'
        """
        return self.sensors.get(data_type)

    def _get_stations(self, data_type: str, sensor: str):
        """
        Returns a list of available sstations for a given sensor
        """
        url = f"{self.base_url}/{data_type}"
        params = {"ajax": "1", "sensor": sensor}
        
        response = self.client.get(url, params=params)
        data = response.json()
        
        df = pd.DataFrame(data)
        df = df.T.reset_index(drop=True)
        
        return df
    
    def get_historical_met_stations(self, sensor: str):
        df = self._get_stations(data_type='clima-historicos', sensor=sensor)
        return df

    def get_historical_averages(self, sensor: str, station_id: str):
        pass

    def get_high_frequency_data(self, station_id, sensor):
        url = f"{self.base_url}/estaciones-satelitales-data"
        params = {"estacion": station_id, "sensor": sensor, "ajax": "1"}
        
        response = self.client.get(url, params=params)
        data_dict = response.json()
        
        df = pd.DataFrame(data_dict['datos'], columns=['timestamp', 'value'])
        df['date_time'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.loc[:, ['date_time', 'value']]
        return df