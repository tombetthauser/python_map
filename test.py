import folium
print(dir(folium))
map = folium.Map(location=[80,-100])
map.save("Map.html")
