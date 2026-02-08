"""
Example and sandbox for imhpa-api
M. G. Castrellon | February 2026
"""

# Load libraries
import imhpa

# Initialize the client
client = imhpa.ImhpaClient()

# Get a list of all station IDs for rain
# stations = client.list_stations(
#     data_type="clima-historicos",
#     sensor="LLUVIA"
# )

# Get a dataframe of historical climate stations
stations = client.get_historical_met_stations(sensor="LLUVIA")
print(stations.loc[stations['rio'] == 'RIO CHAGRES'])

# Get high frequency data for a station
df = client.get_high_frequency_data(station_id="118005", sensor="LLUVIA")
print(df.tail())

# Save to the "Gigantic" database efficiently
# df.to_parquet("2026_rain_data.parquet")