import folium
import geopy
import geopandas
import os

name = input("Please enter your name: ")
city = input("Please enter your studio location (address, city, country): ")

locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')
location = locator.geocode(city)

# map = folium.Map(location=[80,-100])
# map.save("Map.html")
# map2 = folium.Map(location=[38.58,-99.09], zoom_start=6)
# map2.save("Map2.html")

map3 = folium.Map(location=[location.latitude,location.longitude], zoom_start=10, tiles="Stamen Terrain")
map3.add_child(folium.Marker(location=[location.latitude,location.longitude], popup=f"{name}'s' Studio", icon=folium.Icon(color='green')))
map3.save("Map3.html")

# print('Latitude={}, Longitude={}'.format(location.latitude, location.longitude))
os.system('open Map3.html')