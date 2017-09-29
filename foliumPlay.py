#Danaya Melendez
#CMP 464 - Data Science
#Prof. Owen

import folium
import pandas as pd
import math

crash = pd.read_csv('birthdayCrashes.csv')

map1 = folium.Map(location=[40.75, -74.125])

for index,row in crash.iterrows():
    if not (math.isnan(row["LATITUDE"])):
        lat = row["LATITUDE"]
        lon = row["LONGITUDE"]
        folium.Marker([lat, lon],icon=folium.Icon(color='red')).add_to(map1)

map1.save('/Users/danayamelendez/PyCharmProjects/CMP 464/crashes.html')

lehman = pd.read_csv('wifiHotspots.csv')

map2 = folium.Map(location=[40.8044341,-73.945772])

for index,row in lehman.iterrows():
        lat = row["LAT"]
        lon = row["LON"]
        if ((lat > 40.7944341 and lat < 40.8144341) and (lon < -73.935772 and  lon > -73.955772)):
            if (row["LOCATION_T"] == "Indoor"):
                folium.Marker([lat, lon], icon=folium.Icon(color='blue')).add_to(map2)
            else:
                folium.Marker([lat, lon],icon=folium.Icon(color='green')).add_to(map2)


map2.save('/Users/danayamelendez/PyCharmProjects/CMP 464/wifi.html')