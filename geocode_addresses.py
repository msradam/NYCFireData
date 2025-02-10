# Adam Munawar Rahman, March 2020
# Geocodes addresses using geopy and adds a lat-long column to a given .csv

from geopy.geocoders import Nominatim, GoogleV3
from geopy.exc import GeocoderTimedOut
import csv
import pandas as pd

import time

geolocator = Nominatim(user_agent="heattweet_string4", timeout=40)

fdny_df = pd.read_csv("csv-data/fdny_data_excerpt.csv")


def geocode_address(locator, address):
    """
    Takes in a geopy locator object and address string,
    returns lat-long tuple
    """
    location = locator.geocode(address)
    try:
        if location == None:
            return (float("nan"), float("nan"))
        else:
            return (location.latitude, location.longitude)
    except GeocoderTimedOut:
        raise


# print(geocode_address(geolocator,fdny_df['street'][0]))
# Returns (49.211733113006055, -122.82276577153996)

# Debugging through for loop over column

# geocoded_coordinates = []
# for address in fdny_df['street']:
#     latlong = geocode_address(geolocator, address)
#     print(latlong)
#     geocoded_coordinates.append(latlong)
#     #print(address)
#     time.sleep(2) # Guardrail to avoid potential rate-limiting against nominatim API

# fdny_df['lat-long'] = geocoded_coordinates
# print(fdny_df['lat-long'])

# Concise method - use df.apply to map function across column and insert as new column
fdny_df["lat-long"] = fdny_df["street"].apply(
    lambda address: geocode_address(geolocator, address)
)

fdny_df.to_csv("csv-data/fdny_data_excerpt_geo_code.csv")
