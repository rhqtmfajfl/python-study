# import folium

# m= folium.Map(location=[45.])


import pandas as pd
import numpy as np
import folium as g
from folium.plugins import HeatMap



g_map = g.Map(location=[34.8166,127.9264],zoom_start=18) #처음에는 맵부터 띄운다.

# option

marker = g.Marker([34.8166,127.9264], # 마커를 찍는 과정이다. 해당 위치의  마커를 찍고

                 popup='campus seven', # 해당 마커의 이름을 넣어준다.

                 icon = g.Icon(color='blue'), # 해당 아이콘의 색깔을 지정해준다.

                 )
marker02 = g.CircleMarker([34.8166,127.9264], # CircleMarker를 통해 원형으로 보이게 한다.
                         radius=100,		# 범위
                         color='skyblue',	# 선 색깔
                         popup='campus seven', # 원의 의름
                          fill_color = 'skyblue' # 채워질 원의 색깔
                         )
marker02.add_to(g_map) # 위에서 만들었던 map에 반영된다.

energy = pd.read_excel('c:/dd/main.xlsx')
#max_energy = pd.read_excel('c:/dd/한국남동발전_발전실적 (1).xlsx')

# max_energy.columns = ['loc', 'plant', 'date', 'storage', 'energy', 'hot', 'use', 'generator']
# df2 = energy[energy['generator'] == '태양력'].copy()

# df3 = df2['EG'].max()

#data_energy = energy[['사업소','실제위도','실제경도','지점코드','위치','위도','경도','비고']]
#data_energy2 = data_energy[data_energy['위치'] == '남해군']
#data_energy2[data_energy2['위치'].str.contains('남해군')]

# for i in range(len(data_energy2)):
#     marker01 = g.Marker([data_energy2.loc[i]['위도'], data_energy2[i]['경도']],
#                  popup = data_energy2.loc[i]['사업소'],
#                  icon = g.Icon(color='skyblue'))
#     marker01.add_to(g_map)            

# for i in range(len(energy)):
#          marker01 = g.Marker([energy.loc[i]['위도'], energy[i]['경도']],
                  
#                   icon = g.Icon(color='skyblue'))
#          marker01.add_to(g_map)
#a= max_energy['발전량(MWh)'].max()

for i in energy.index:

        if df3 >= 1000: 
         sub_lat = energy.loc[i, 'latitude']
         sub_long = energy.loc[i, 'longitude']

         


         g.Marker([sub_lat, sub_long]).add_to(g_map)
#파일 읽기
#print(energy.head(10))

marker.add_to(g_map) # 마지막으로 위에 만들었던 맵에다가 marker를 add 해준다.
#marker01.add_to(g_map)

g_map.save('.now_location_map.html')

g_map # 그 후 g_map을 본다.
