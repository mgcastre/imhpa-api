"""
Example and sandbox for imhpa-api
M. G. Castrellon | February 2026
"""

# Load libraries
import os
import src.imhpa as imhpa

# Initialize the client
client = imhpa.ImhpaClient()

# Define a list of sensors to retrieve data for
my_sensors = [
    'HR_PROM',
    'LLUVIA',
    'NIVEL',
    'P_BAROM',
    'RAD_SOLAR',
    'TEMP_PROM',
]

# Define path to save the data
local_dir_out = "D:/Dropbox/Panama_Data/IMHPA/raw"
if not os.path.exists(local_dir_out):
    os.makedirs(local_dir_out)

#  Loop through sensors and stations to retrieve and save data
for sensor in my_sensors:
    print(f"Processing sensor: {sensor}")

    output_path = f"{local_dir_out}/{sensor}"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    stations_df = client.get_stations(sensor=sensor)
    print(f"Found {len(stations_df)} stations for sensor {sensor}")
    
    list_of_dfs = []
    for station_id in stations_df['id']:
        print(f"Processing station: {station_id}")
        data_df = client.get_data(sensor=sensor, station_id=station_id)
        data_df.to_parquet(f"{output_path}/{sensor}_{station_id}.parquet")

