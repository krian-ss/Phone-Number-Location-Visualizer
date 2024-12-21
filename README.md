# Phone-Number-Location-Visualizer
Set Up Your Environment:

- Ensure you have Python installed on your system.

- Install the required libraries if you haven't already. You can do this using pip:
pip install phonenumbers folium opencage-geocoder

Prepare the Code:

- Create a new Python file (e.g., main.py) and copy the following code into it:

import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

# Replace with your OpenCage API key
Key = 'your_api_key_here'

# Define the phone number you want to track
num = "+911234567890"  # Replace with the desired phone number

# Retrieve location information
sanNumber = phonenumbers.parse(num)
yourLocation = geocoder.description_for_number(sanNumber, "en")
print('Location:', yourLocation)

# Retrieve service provider information
service_provider = phonenumbers.parse(num)
print('Service provider:', carrier.name_for_number(service_provider, "en"))

# Geocode the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
result = geocoder.geocode(query)

# Extract latitude and longitude
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

# Create a map
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# Save the map as an HTML file
myMap.save("myLocation.html")

Insert Your API Key:

- Sign up for an OpenCage Geocoding API key if you don't have one. Replace 'your_api_key_here' in the code with your actual API key.

Run the Code:

- Execute the script by running the following command in your terminal or command prompt:
python main.py

View the Results:

- After running the code, it will print the location and service provider information to the console.

- The code will also generate an HTML file named myLocation.html. Open this file in a web browser (e.g., Chrome) to view the interactive map with the location of the phone number marked.

Modify as Needed:

- You can change the phone number in the num variable to track a different number.

- Adjust the zoom level in the folium.Map() function if you want to change how zoomed in the map is.
