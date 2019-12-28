#%% 

import random

random.random()



# %%

random.randint(-90,90)

# %%

x = 1
latitudes = []
while x < 11:
    random_lat = random.randint(-90, 90) + random.random()
    latitudes.append(random_lat)
    x += 1

latitudes

# %%
random.randrange(-90, 90, step=180)

# %%
# Import timeit.
import timeit
# Import the NumPy module.
import numpy as np

%timeit np.random.uniform(-90.000, 90.000, size=1500)

# %%
def latitudes(size):
    latitudes = []
    x = 0
    while x < (size):
        random_lat = random.randint(-90, 90) + random.random()
        latitudes.append(random_lat)
        x += 1
    return latitudes
# Call the function with 1500. 
%timeit latitudes(1500)

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
# Create a practice set of random latitude and longitude combinations.
x = [25.12903645, 25.92017388, 26.62509167, -59.98969384, 37.30571269]
y = [-67.59741259, 11.09532135, 74.84233102, -76.89176677, -61.13376282]
coordinates = zip(x, y)


# %%
# Use the tuple() function to display the latitude and longitude combinations.
for coordinate in coordinates:
    print(coordinate[0], coordinate[1])

# %%
# Add the latitudes and longitudes to a list.
coordinates = list(lat_lngs)

# %%
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



# %%
