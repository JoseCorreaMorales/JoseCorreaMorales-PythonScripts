# Import necessary libraries
import geocoder 
import folium

# Get location of phone
g = geocoder.ip('me')
location = g.latlng


# Create map with location of phone
m = folium.Map(location=location, zoom_start=15)
folium.Marker(location=location, popup='Phone Location').add_to(m)

# Save map to file
m.save('phone_location.html')

# This script is intended 
# for educational purposes only and should not be used for illegal activities.'

# pip3 install geocoder folium