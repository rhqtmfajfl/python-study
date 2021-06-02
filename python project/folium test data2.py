import pandas as pd
import numpy as np
import folium as g
from folium.plugins import HeatMap

g_map = g.Map(location=[34.8166,127.9264],zoom_start=18) #처음에는 맵부터 띄운다.
energy = pd.read_excel('c:/dd/main.xlsx')

df3 = energy['EG'].max()
print(df3)

for i in energy.index:
         sub_lat = energy.loc[i, 'latitude']
         sub_long = energy.loc[i, 'longitude']

         kkk = [sub_lat, sub_long]

if df3 >=1085:
        ace = kkk
g.Marker(ace).add_to(g_map)

g_map.save('.now_location_map.html')

g_map #g_map을 본다.


