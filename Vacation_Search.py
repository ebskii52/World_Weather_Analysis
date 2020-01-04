# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
## Import the dependencies.
import pandas as pd
import gmaps
import requests

# Import the API key.
from config import g_key


# %%
# Store the CSV you saved created in part one into a DataFrame.
city_weather_df = pd.read_csv("data/WeatherPy_challenge.csv")
city_weather_df.rename(columns={"Rain Inches (last 3hours)":"RainInches", "Snow Inches (last 3hours)":"SnowInches"}, inplace=True)
city_weather_df.head()


# %%
# Configure gmaps to use your Google API key.
gmaps.configure(api_key=g_key)


# %%
# Ask the customer to add a minimum and maximum temperature value.
min_temp = float(input("What is the minimum temperature you would like for your trip? "))
max_temp = float(input("What is the maximum temperature you would like for your trip? "))
raining = input("Do you want it to be raining? (yes/no) ")
snowing = input ("Do you want it to be snowing? (yes/no) ")


# %%
preferred_cities_df = city_weather_df.loc[(city_weather_df["Max Temp"] <= max_temp) & (city_weather_df["Max Temp"] >= min_temp)]
if (raining == "yes"):
    preferred_cities_df = preferred_cities_df.loc[(preferred_cities_df["RainInches"] > 0)]
elif (snowing == "yes"):
    preferred_cities_df = preferred_cities_df.loc[(preferred_cities_df["SnowInches"] > 0)] 
    
preferred_cities_df.head(10)


# %%
preferred_cities_df.count()


# %%
# Create DataFrame called hotel_df to store hotel names along with city, country, max temp, and coordinates.
hotel_df = preferred_cities_df[["City", "Country", "Max Temp",  "Current Description", "Lat", "Lng"]].copy()
hotel_df["Hotel Name"] = ""
hotel_df.head(10)


# %%
# Set the parameters to search for a hotel in Paris.
params = {
    "radius": 5000,
    "types": "lodging",
    "key": g_key,
    "location": "48.8566, 2.3522"}

# Iterate through the DataFrame.
for index, row in hotel_df.iterrows():
    # Get the latitude and longitude.
    lat = row["Lat"]
    lng = row["Lng"]

    # Add the latitude and longitude to the params dictionary as values to the location key.
    params["location"] = f"{lat},{lng}"

    # Use the search term: "lodging" and our latitude and longitude.
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    # Make request and get the JSON data from the search.
    hotels = requests.get(base_url, params=params).json()
     # Grab the first hotel from the results and store the name.
    try:
        hotel_df.loc[index, "Hotel Name"] = hotels["results"][0]["name"]
    except (IndexError):
        print("Hotel not found... skipping.")
    


# %%
hotel_df.head(10)
  


# %%
info_box_template = """
<dl>
<dt>Hotel Name</dt><dd>{Hotel Name}</dd>
<dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
<dt>Current Weather</dt><dd>{Current Description} and {Max Temp} °F</dd>
</dl>
"""


# %%
# %%
# Store the DataFrame Row.
hotel_info = [info_box_template.format(**row) for index, row in hotel_df.iterrows()]


# %%
# Add a heatmap of temperature for the vacation spots and a pop-up marker for each city.
locations = hotel_df[["Lat", "Lng"]]
max_temp = hotel_df["Max Temp"]
fig = gmaps.figure(center=(30.0, 31.0), zoom_level=1.5)
marker_layer = gmaps.marker_layer(locations, info_box_content=hotel_info)
fig.add_layer(marker_layer)

#embed_minimal_html('export.html', views=[fig])

# Save the figure.
#fig.save("weather_data/Hotels.png")

# Call the figure to plot the data.
fig


# %%
## Upload the CSV file as part of your submission as WeatherPy_challenge.csv.

# Create the output file (CSV).
output_data_file = "data/WeatherPy_vacation.csv"

# Export the City_Data into a CSV.
hotel_df.to_csv(output_data_file, index_label="City_ID")

