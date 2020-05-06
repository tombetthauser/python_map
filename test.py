import folium
print(dir(folium))
map = folium.Map(location=[80,-100])
map.save("Map.html")
map2 = folium.Map(location=[38.58,-99.09], zoom_start=6)
map2.save("Map2.html")
