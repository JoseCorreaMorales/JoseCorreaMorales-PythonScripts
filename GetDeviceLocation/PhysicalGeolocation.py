""" The script by IP uses an IP address to determine the location, 
which can be different from the physical location of the device.
 To get the physical location of the device, its necessary to
   use other methods such as GPS or WiFi triangulation.
 However, these methods typically require access to the
   device itself and may not be possible in all situations.
    
One way to do this is by using a combination of WiFi triangulation and geolocation
 APIs. Here's an example script that uses the Google Maps API to get the physical
   location of a device based on WiFi network information
        """
import requests

# Function to get the physical location of a device based on WiFi network information
def get_location():
    # Get the list of WiFi networks in range
    networks = [
        {"macAddress": "01:23:45:67:89:AB"},
        {"macAddress": "CD:EF:01:23:45:67"}
    ] # Replace with the actual MAC addresses of the nearby WiFi networks
    
    # Make a request to the Google Maps API to get the physical location of the device
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY"
    response = requests.post(url, json={"wifiAccessPoints": networks})
    
    # Extract the latitude and longitude from the response
    if response.status_code == 200:
        location = response.json()["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return latitude, longitude
    else:
        return None

# Call the get_location() function to get the physical location of the device
location = get_location()
if location:
    print(f"Latitude: {location[0]}, Longitude: {location[1]}")
else:
    print("Unable to determine location.")