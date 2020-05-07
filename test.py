import folium
import geopy
import geopandas
# print(dir(folium))
map = folium.Map(location=[80,-100])
map.save("Map.html")
map2 = folium.Map(location=[38.58,-99.09], zoom_start=6)
map2.save("Map2.html")
map3 = folium.Map(location=[38.58,-99.09], zoom_start=10, tiles="Stamen Terrain")
map3.add_child(folium.Marker(location=[38.58,-99.09], popup="Tom Betthauser's Studio", icon=folium.Icon(color='green')))
map3.save("Map3.html")

locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')
# locator = Nominatim(user_agent='myGeocoder')
location = locator.geocode("Champ de Mars, Paris, France")

print('Latitude={}, Longitude={}'.format(location.latitude, location.longitude))
