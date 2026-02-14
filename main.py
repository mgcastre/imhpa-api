"""
Example and sandbox for imhpa-api
M. G. Castrellon | February 2026
"""

# Load libraries
import imhpa

# Initialize the client
client = imhpa.ImhpaClient()

# Get a list of all sensors
print(client.get_sensors())

# # Obtain data from station "EL MARIA"
# data = client.get_data(sensor='LLUVIA', station_id='118005')

# # Save data to a feather file
# data.to_feather("../local/rain_data.ftr")