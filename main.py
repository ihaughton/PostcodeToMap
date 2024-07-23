import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from tqdm import tqdm

# Initialize geolocator
geolocator = Nominatim(user_agent="postcode_map_project")

# Function to geocode postcode
def geocode_postcode(postcode):
    try:
        location = geolocator.geocode(postcode)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        return geocode_postcode(postcode)

# Load postcode data
postcode_data = pd.read_csv('postcode_data.csv')

# Create a global map using Folium
global_map = folium.Map(location=[0, 0], zoom_start=2)

# Iterate through postcode data and add markers to the map
for index, row in tqdm(postcode_data.iterrows(), total=postcode_data.shape[0], desc="Geocoding postcodes"):
    postcode = row['Postcode']
    coordinates = geocode_postcode(postcode)
    
    if coordinates:
        latitude, longitude = coordinates
        # Add a marker for each postcode
        folium.Marker(
            location=[latitude, longitude],
            popup=postcode
        ).add_to(global_map)
    else:
        print(f"Could not geocode postcode: {postcode}")

# Save the map as an HTML file
global_map.save("postcode_map.html")
