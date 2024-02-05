#
# Ciaran Moran
# G00426050@atu.ie
# Assignment: current weather
#
import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
response = requests.get(url)
#print (response.json())
data = response.json()

#this is an example of the data that the URL returns
#{"latitude":53.82,"longitude":-9.5,"generationtime_ms":0.04398822784423828,
#"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":54.0,
#"current_units":{"time":"iso8601","interval":"seconds","temperature_2m":"°C","wind_speed_10m":"km/h"},
#"current":{"time":"2024-02-05T13:15","interval":900,"temperature_2m":11.2,"wind_speed_10m":25.2}}

# This sets the unit for the weather measurements
# Useful info and looks nice when displaying! 
current_units = data["current_units"]
current_units_temp_2m = current_units["temperature_2m"] 
current_units_wind_10m = current_units["wind_speed_10m"] 

# Now set the current weather temp and wind
current = data["current"]
#print(current)
current_temp = current["temperature_2m"]
current_wind = current["wind_speed_10m"]

# Now display the weather readings for temp and wind...
print("Current Temperature (2 m):", current_temp, current_units_temp_2m)
print("Current Wind (10 m):", current_wind, current_units_wind_10m)

