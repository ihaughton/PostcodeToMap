import pandas as pd
import folium
import pdfkit
from folium import FeatureGroup

# Step 1: Load postcode data
postcode_data = pd.read_csv('postcode.csv')

# Step 2: Create a UK map using Folium
uk_map = folium.Map(location=[54.7023545, -3.2765753], zoom_start=6)
#marker_map = FeatureGroup(name="Markers")

# Step 3 & 4: Iterate through postcode data and add markers to the map
for index, row in postcode_data.iterrows():
    
    postcode = row.str.split()[0][0]
    latitude = float(row.str.split()[0][1])
    longitude = float(row.str.split()[0][2])

    print(f"index: {index}")
    print(f"postcode: {postcode}")
    print(f"latitude: {latitude}")
    print(f"longitude: {longitude}")

    #postcode = row['Postcode']
    #latitude = row['Latitude']
    #longitude = row['Longitude']
    
    # Step 5: Add a marker for each postcode
    folium.Marker(
        location=[latitude, longitude],
        popup=postcode
    ).add_to(uk_map)

#marker_map.add_to(uk_map)
    
# Step 6: Save the map as an HTML file
uk_map.save("postcode_map.html")

# Create pdf version
pdfkit_config = pdfkit.configuration()
pdfkit.from_file("postcode_map.html", "postcode_map.pdf", configuration=pdfkit_config)
