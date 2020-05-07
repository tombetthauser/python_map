import folium
import geopy
import geopandas
import os

os.system('clear')

cities = []
names = {}
websites = {}
userinput = False

print('\n\nWelcome to the studio map generator, a way to visualize artist studios in a given area.\n')
print('Please add names and addresses for artist studios below.')
print('Make sure to enter addresses carefully or the program will crash because it sucks.')
print('Addresses hould be entered as such: "3198 Swallows Nest Drive, Sacramento, United States".')
print('When complete enter "done" or enter no information for both address and artists name.')
print('After this your browser will open with a map for all the locations you entered.')

title = input('\nFirst, please enter the full text of what you want your websites title to be: ')

while userinput not in ('done', 'finished', 'complete', 'next', ''):
  userinput = input("\nPlease enter an artist's studio location (address, city, country): ")
  cities.append(userinput)
  if userinput in ('done', 'finished', 'complete', 'next', ''):
    break
  userinput = input("Please enter that artist's name: ")
  names[cities[len(cities)-1]] = userinput
  if userinput in ('done', 'finished', 'complete', 'next', ''):
    break
  userinput = input("Please enter that artist's website: ")
  websites[cities[len(cities)-1]] = userinput

print('\nAll addresses entered, please wait for map to be generated, it will open automatically.\n')

cities.pop()

locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')
location = locator.geocode(cities[0])

# map = folium.Map(location=[80,-100])
# map.save("Map.html")
# map2 = folium.Map(location=[38.58,-99.09], zoom_start=6)
# map2.save("Map2.html")

# print("\n\ncities array ------")
# print(cities)
# print("\ncities array ------")
# print(names)
# print("\n\n")

map3 = folium.Map(location=[location.latitude,location.longitude], zoom_start=14, tiles="CartoDB positron")
for c in cities:
  location = locator.geocode(c)
  # print("\n Start new child -----")
  # print(c)
  # print(location)
  # print(location.latitude)
  # print(location.longitude)
  # print(names[c])
  map3.add_child(folium.Marker(location=[location.latitude, location.longitude], popup=f"{names[c]}'s' Studio\n{websites[c]}", icon=folium.Icon(color='blue')))
  # print("New child added -----\n\n")

map3.save("Map3.html")


f = open("Map3.html", "r")
contents = f.readlines()
f.close()

username = "Erin"

userdiv = "<div class = 'user-title-div' style = 'text-align: center; height: 200px; font-size: 25px; line-height: 200px;'>Erin's Open Studios Map</div>"
contents.insert(
    37, f"<div class = 'user-title-div' style = 'text-align: center; height: 200px; font-size: 25px; line-height: 200px;'>{title}</div>")


f = open("Map3.html", "w")
contents = "".join(contents)
f.write(contents)
f.close()



# print('Latitude={}, Longitude={}'.format(location.latitude, location.longitude))
os.system('open Map3.html')
