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
vacation_weather_df = pd.read_csv("data/WeatherPy_vacation.csv")
#vacation_weather_df.rename(columns={"Rain Inches (last 3hours)":"RainInches", "Snow Inches (last 3hours)":"SnowInches"}, inplace=True)
vacation_weather_df[vacation_weather_df["Country"] == "FR"].head(10)


# %%
cities_to_visit = [ "Souillac", "Ronne","Veraval", "Saint-Pierre"]
    
CityDF = vacation_weather_df.loc[(vacation_weather_df["City"] == cities_to_visit[0])  | (vacation_weather_df["City"] == cities_to_visit[1]) | (vacation_weather_df["City"] == cities_to_visit[2]) | (vacation_weather_df["City"] == cities_to_visit[3])]

CityDF

#CityVacationDF = pd.DataFrame(CitiesArray)
#CityVacationDF


# %%

latitudes = []
longitudes = []

# Iterate through the DataFrame.
for index, row in CityDF.iterrows():
    # Get the latitude and longitude.
    lat= row["Lat"]
    lng= row["Lng"]

    latitudes.append(lat)
    longitudes.append(lng)




# %%
import gmaps
import gmaps.datasets
gmaps.configure(api_key=g_key)

# Latitude-longitude pairs
Souillac = (latitudes[0],longitudes[0])
Ronne = (latitudes[1],longitudes[1])

Veraval = (latitudes[2],longitudes[2])

SaintPierre = (latitudes[3],longitudes[3])

fig = gmaps.figure()

Souillac2SaintPierre_via_Ronne_via_Veraval = gmaps.directions_layer(
        Souillac, Veraval, waypoints=[Ronne,SaintPierre],
        travel_mode='DRIVING')
fig.add_layer(Souillac2SaintPierre_via_Ronne_via_Veraval)
fig


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

# Store the DataFrame Row.
hotel_info = [info_box_template.format(**row) for index, row in CityDF.iterrows()]


# %%
# Add a heatmap of temperature for the vacation spots and a pop-up marker for each city.
locations = CityDF[["Lat", "Lng"]]
max_temp = CityDF["Max Temp"]
fig = gmaps.figure(center=(45.60, -0.60	), zoom_level=5)
marker_layer = gmaps.marker_layer(locations, info_box_content=hotel_info)
fig.add_layer(marker_layer)

#embed_minimal_html('export.html', views=[fig])

# Save the figure.
#fig.save("weather_data/Hotels.png")

# Call the figure to plot the data.
fig


# %%


