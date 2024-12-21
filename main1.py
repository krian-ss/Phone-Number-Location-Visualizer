import phonenumbers
import folium

from phonenumbers import geocoder
from number import num

Key='Your_API'
from phonenumbers import geocoder

sanNumber=phonenumbers.parse(num)

yourLocation=geocoder.description_for_number(sanNumber,"en")

print('Location:',yourLocation)

#service provider

from phonenumbers import carrier

service_provider=phonenumbers.parse(num)

print('Service provider:',carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(Key)

query=str(yourLocation)

result=geocoder.geocode(query)

print(result)

lat=result[0]['geometry']['lat']

lng=result[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

#save map in html

myMap.save("myLocation.html")
