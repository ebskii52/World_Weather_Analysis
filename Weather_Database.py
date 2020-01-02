#%%
# Import the dependencies.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a set of random latitude and longitude combinations.
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)
lat_lngs

#lats
# %%
coordinates = list(lat_lngs)
coordinates

# %%
# Import the requests library.
import requests

# Import the API key.
from config import weather_api_key

# %%
# Starting URL for Weather Map API Call.
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key
url

#%%
from citipy import citipy
for coordinate in coordinates:
    print(citipy.nearest_city(coordinate[0], coordinate[1]).city_name , citipy.nearest_city(coordinate[0], coordinate[1]).country_code)

# %%
# Create a list for holding the cities.
cities = []
# Identify the nearest city for each latitude and longitude combination.
for coordinate in coordinates:
    city = citipy.nearest_city(coordinate[0], coordinate[1]).city_name    
    # If the city is unique, then we will add it to the cities list.
    if city not in cities:
        cities.append(city)
# Print the city count to confirm sufficient count.
cities

#%%
# Import the datetime module from the datetime library.
from datetime import datetime

# Create an empty list to hold the weather data.
city_data = []
# Print the beginning of the logging.
print("Beginning Data Retrieval     ")
print("-----------------------------")

# Create counters.
record_count = 1
set_count = 1

# %%
# Loop through all the cities in the list.
for i, city in enumerate(cities):

    # Group cities in sets of 50 for logging purposes.
    if (i % 50 == 0 and i >= 50):
        set_count += 1
        record_count = 1
    # Create endpoint URL with each city.
    city_url = url + "&q=" + city

    # Log the URL, record, and set numbers and the city.
    print(f"Processing Record {record_count} of Set {set_count} | {city}")
    # Add 1 to the record count.
    record_count += 1

    # Run an API request for each of the cities.
    try:
        # Parse the JSON and retrieve data.
        city_weather = requests.get(city_url).json()
        # Parse out the needed data.
        city_lat = city_weather["coord"]["lat"]
        city_lng = city_weather["coord"]["lon"]
        city_max_temp = city_weather["main"]["temp_max"]
        city_humidity = city_weather["main"]["humidity"]
        city_clouds = city_weather["clouds"]["all"]
        city_wind = city_weather["wind"]["speed"]
        city_country = city_weather["sys"]["country"]
        city_description = city_weather["weather"]
        weather_description = city_description[0]["description"] 

        try:
            city_snow =  city_weather["snow"]["3h"]
        except:
            city_snow = 0
        
        try:
            city_rains =  city_weather["rain"]["3h"]
        except:
            city_rains = 0
            
           
       
        # Convert the date to ISO standard.
        city_date = datetime.utcfromtimestamp(city_weather["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        # Append the city information into city_data list.
        city_data.append({"City": city.title(),
                          "Country": city_country,
                          "Date": city_date,
                          "Lat": city_lat,
                          "Lng": city_lng,
                          "Max Temp": city_max_temp,
                          "Humidity": city_humidity,
                          "Cloudiness": city_clouds,
                          "Wind Speed": city_wind,
                          "Current Description": weather_description,
                          "Rain Inches (last 3hours)": city_rains,
                          "Snow Inches (last 3hours)": city_snow})             

# If an error is experienced, skip the city.
    except:
        print("City not found. Skipping...")
        pass

# Indicate that Data Loading is complete.
print("-----------------------------")
print("Data Retrieval Complete      ")
print("-----------------------------")
   

# %%
# Convert the array of dictionaries to a Pandas DataFrame.
city_data_df = pd.DataFrame(city_data)
city_data_df.head(20)

#%%
## Upload the CSV file as part of your submission as WeatherPy_challenge.csv.
# Create the output file (CSV).
output_data_file = "weather_data/WeatherPy_challenge.csv"
# Export the City_Data into a CSV.
city_data_df.to_csv(output_data_file, index_label="City_ID")

#%%
# Answer this question using Pandas methods: How many cities have recorded rainfall or snow?
Rainfall_Snow_Count = city_data_df.loc[(city_data_df["Rain Inches (last 3hours)"]>0) | (city_data_df["Snow Inches (last 3hours)"]>0)]
Rainfall_Snow_Count["City"].count()

# %%
