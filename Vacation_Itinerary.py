#%%
## Import the dependencies.
import pandas as pd
import gmaps
import requests
# Import the API key.
from config import g_key

# %%
# Store the CSV you saved created in part one into a DataFrame.
vacation_weather_df = pd.read_csv("data/WeatherPy_vacation.csv")
vacation_weather_df[vacation_weather_df["Country"] == "FR"].head(10)

# %%
cities_to_visit = ["Ronne", "Estelle", "Saint-Pierre", "Veraval"]
    
CityDF = vacation_weather_df.loc[(vacation_weather_df["City"] == cities_to_visit[0])  | (vacation_weather_df["City"] == cities_to_visit[1]) | (vacation_weather_df["City"] == cities_to_visit[2]) | (vacation_weather_df["City"] == cities_to_visit[3])]
CityDF

#%%

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
Ronne = (latitudes[0],longitudes[0])
Estelle = (latitudes[1],longitudes[1])
Saint-Pierre = (latitudes[2],longitudes[2])
Veraval = (latitudes[3],longitudes[3])

fig = gmaps.figure()
geneva2zurich = gmaps.directions_layer(Ronne, Estelle, Saint-Pierre, Veraval)
fig.add_layer(geneva2zurich)
fig

# %%
