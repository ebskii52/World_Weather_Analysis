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

# %%
