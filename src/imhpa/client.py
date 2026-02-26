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
    def __init__(self, timeout: float = 10.0):
        self.client = httpx.Client(timeout=timeout)
        self.base_url = "https://www.imhpa.gob.pa/es"
        self.url_satellite = f"{self.base_url}/estaciones-satelitales"

    def _fetch_sensors(self) -> dict:
        """Fetches raw sensor dict from the IMHPA website."""
        response = self.client.get(self.url_satellite)

        soup = BeautifulSoup(response.text, "lxml")
        script_tag = soup.find('script', string=re.compile(r'var sensores_satelital'))

        pattern = r'var sensores_satelital\s*=\s*(\{.*?\});'
        match = re.search(pattern, script_tag.string, re.DOTALL)

        if match:
            json_data = json.loads(match.group(1))
        else:
            raise RuntimeError(f"Could not extract sensors from {self.url_satellite}")

        return json_data

    def list_sensors(self, code: bool = False) -> list:
        """
        Returns a list of available sensor labels (default) or codes.

        Parameters
        ----------
        code : bool
            If True, returns code names of the sensors.
        """
        raw = self._fetch_sensors()
        return list(raw.keys()) if code else list(raw.values())

    def get_sensors(self) -> pd.DataFrame:
        """Return a DataFrame of all sensors with their codes and labels."""
        raw = self._fetch_sensors()
        return pd.DataFrame(raw.items(), columns=["code", "label"])

    def _fetch_stations(self, sensor: str) -> dict:
        """
        Fetches raw station dict from the IMHPA website.
        Requires the sensor code as an input parameter.
        """
        url = f"{self.url_satellite}-data2"
        response = self.client.get(url, params=dict(sensor=sensor))
        return response.json()

    def list_stations(self, sensor: str, ids: bool = False) -> list:
        """
        Returns a list of available station names (default) or ids for a given sensor.

        Parameters
        ----------
        sensor : str
            Sensor code as given by the list_sensors method.
        labels : bool
            If False, returns a list of station ids.
        """
        raw = self._fetch_stations(sensor)
        stations = raw.get('estaciones')
        if ids:
            return list(stations.keys())
        return [x['nombre'] for x in stations.values()]

    def get_stations(self, sensor: str) -> pd.DataFrame:
        """
        Returns a dataframe with the stations available for a given sensor and their metadata.
        Requires the sensor code as an input parameter.
        """
        raw = self._fetch_stations(sensor)
        df = pd.DataFrame(raw.get('estaciones'))
        df = df.T.reset_index().rename(columns={"index":"id"})

        for col in df.columns:
            df[col] = df[col].convert_dtypes()
        
        for col in ["latitud", "longitud"]:
            df[col] = df[col].astype(float)
        
        for col in ["id", "numero_estacion"]:
            df[col] = df[col].astype(int)

        return df

    def _fetch_data(self, station_id: str, sensor: str) -> dict:
        """
        Fetch raw JSON data from the IMHPA API for a given station and sensor.

        Parameters
        ----------
        station_id : str
            The station identifier (e.g. '118005').
        sensor : str
            The sensor code (e.g. 'LLUVIA').

        Returns
        -------
        dict
            Raw JSON response from the API, including readings and metadata.
        """
        data_url = f"{self.url_satellite}-data"
        params = {"estacion": station_id, "sensor": sensor, "ajax": "1"}
        response = self.client.get(data_url, params=params)
        return response.json()

    def get_data(self, station_id: str, sensor: str) -> pd.DataFrame:
        """
        Return sensor readings for a given station as a tidy DataFrame.

        The raw millisecond timestamp from the API is converted to a
        datetime column and dropped in favour of the human-readable value.

        Parameters
        ----------
        station_id : str
            The station identifier (e.g. '118005').
        sensor : str
            The sensor code (e.g. 'LLUVIA').

        Returns
        -------
        pd.DataFrame
            Columns: sensor, station_id, date_time, value, unit.
        """
        raw_data = self._fetch_data(station_id, sensor)

        df = pd.DataFrame(raw_data['datos'], columns=['timestamp', 'value'])
        df['date_time'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.drop(columns=['timestamp'], inplace=True)

        df['station_id'] = station_id
        df['sensor'] = raw_data['sensor']
        df['unit'] = raw_data['unidad_medida']

        col_order = ['sensor', 'station_id', 'date_time', 'value', 'unit']

        return df.loc[:, col_order]

    # def get_historical_met_stations(self, sensor: str):
    #     df = self._get_stations(data_type='clima-historicos', sensor=sensor)
    #     return df

    # def get_historical_averages(self, sensor: str, station_id: str):
    #     pass

