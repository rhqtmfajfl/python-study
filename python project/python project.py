import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#%matplotlib inline
import pandas as pd
#import seaborn as sns
#from matplotlib import font_manager, rc
#font_name = font_manager.FontProperties(fname="c:")
import numpy as np 
import matplotlib.font_manager as fm  
import matplotlib as mpl 
from matplotlib import font_manager, rc
import math
#import plotly.express as px

fin = pd.read_excel('c:/dd/fin.xlsx')

#day = pd.DataFrame()

#month['일자'] = ['2020' + '-' + str(x) for x in range(1,13)]

#a = day.iloc[2194: 2559, 2:4]

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


# df_sample = weather.iloc[:, 0:5] # 앞에는 행 처음부터 끝까지라는 의미, 뒤에는 열을 0에서 5까지 출력


# #df_sample2 = df_sample[df_sample['사업소코드'] == 8630]
# # 
# df_sample3  = weather.sort_values(by ='사업소코드')
# print(df_sample3['사업소코드'].head(1))


# print(weather.head()) #dkv 몇줄
# print(weather.tail())

# # print(weather.describe())

# print(weather.describe(include='all'))

#print(sorted['사업소코드'].head())

# weather.head(3)
# #weather.index()

# #weather.describe()
# print(weather)

#특정 열을 기준으로 잡아 정렬하기

# sorted = weather.sort_values(by = '사업소')

# print(sorted.head(10))

# # #day 열만 출력하기

# print(sorted['사업소', '사업코드'].head(10))


#히스토그램 그리기

# plt.hist(weather)
# plt.show()


#여러 그래프를 그릴때 subplots() 사용

# fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
# fig.set_facecolor('white') ## 캔버스 색상 설정
# ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성
plt.style.use('default')
plt.rcParams['figure.figsize'] = (4,3)
plt.rcParams['font.size'] = 12

fig, ax = plt.subplots()



#ax.plot(day[2194:2558,2:4],day[2194:2558,3:5],color='#c02ad1') ## 선그래프 생성
ax.plot(fin.iloc[2558:2922,2],fin.iloc[2558:2922,10],color='#c02ad1') ## 선그래프 생성
# ax.set_ylim([0, 30])
# plt.plot(fin.iloc[2193:2540,2],fin.iloc[2193:2540,3],color='#c02ad1')
# plt.yticks(np.arange(0,7), ('0','5','10','15','20','25','30'))

ax2 = ax.twinx()

ax2.set_ylabel('발전량', color = 'green')
ax2.plot(fin.iloc[2558:2922,2], fin.iloc[2558:2922,13], color='blue')
# ax2.set_ylim([0,6000])
#ax2.yticks(np.arange(0,7), ('0','5','10','15','20','25','30'))
# ax2.set_yscale('log')
ax2.tick_params(axis='y', labelcolor='green')
#df1 = pd.DataFrame(index = pd.date_range('1/1/2018', periods=100), columns=['온도(℃)'])

#weather.barplot(x=)

#df1.plot()


# plt.xlabel('연도', fontsize = 20)
# plt.ylabel('온도(ºC)', fontsize = 20)
# plt.title('발전량과 온도의 상관관계',fontsize=50) ## 타이틀 설정
plt.show()


# weather.catplot(x="온도(℃)", y="계측일자", hue="smoker",
#             col="time", aspect=.6,
#             kind="swarm", data=tips)