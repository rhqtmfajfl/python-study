import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm  
import matplotlib as mpl 
from matplotlib import font_manager, rc
import datetime
import seaborn as sns

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

fin = pd.read_excel('c:/dd/main.xlsx')

# a = list[fin[0:23]] #2009
# b = fin[24:59]
# c= fin[60:116]
# d= fin[117:225]
# e = fin[226:366]
# f = fin[367:531]
# g = fin[532:699]
# h = fin[700:873]
# i = fin[874:1114]
# j = fin[1115:1378]
# k = fin[1379:1641]
# l = fin[1642:1903] #2020

df = pd.DataFrame(fin)

df2=df[['date']] # 특정 열만 뽑아오기

# print(df2)

#fin.count(a)

# df2 = df2.apply(lambda x : pd.to_datetime(str(x), format='%Y-%m-%d'))

# k= fin.groupby(by='date', as_index=False)

mask = (df2['date'] >= '2009-01-01') & (df2['date'] <= '2009-12-01')
filtered_df = df2.loc[mask]
a= filtered_df.count()

mask = (df2['date'] >= '2010-01-01') & (df2['date'] <= '2010-12-01')
filtered_df = df2.loc[mask]
b= filtered_df.count()

mask = (df2['date'] >= '2011-01-01') & (df2['date'] <= '2011-12-01')
filtered_df = df2.loc[mask]
c= filtered_df.count()

mask = (df2['date'] >= '2012-01-01') & (df2['date'] <= '2012-12-01')
filtered_df = df2.loc[mask]
d= filtered_df.count()

mask = (df2['date'] >= '2013-01-01') & (df2['date'] <= '2013-12-01')
filtered_df = df2.loc[mask]
e= filtered_df.count()

mask = (df2['date'] >= '2014-01-01') & (df2['date'] <= '2014-12-01')
filtered_df = df2.loc[mask]
f= filtered_df.count()

mask = (df2['date'] >= '2015-01-01') & (df2['date'] <= '2015-12-01')
filtered_df = df2.loc[mask]
g= filtered_df.count()

mask = (df2['date'] >= '2016-01-01') & (df2['date'] <= '2016-12-01')
filtered_df = df2.loc[mask]
h= filtered_df.count()

mask = (df2['date'] >= '2017-01-01') & (df2['date'] <= '2017-12-01')
filtered_df = df2.loc[mask]
i= filtered_df.count()

mask = (df2['date'] >= '2018-01-01') & (df2['date'] <= '2018-12-01')
filtered_df = df2.loc[mask]
j= filtered_df.count()

mask = (df2['date'] >= '2019-01-01') & (df2['date'] <= '2019-12-01')
filtered_df = df2.loc[mask]
k= filtered_df.count()

mask = (df2['date'] >= '2020-01-01') & (df2['date'] <= '2020-12-01')
filtered_df = df2.loc[mask]
l= filtered_df.count()

test=[a, b, c, d, e, f, g, h, i, j, k, l]
kkk = pd.DataFrame(test)




# # ?   if fin[2009-01] <= 
# print(fin)

# df2['year'] = df2['date'].dt.year
# mask = df2[df2['year'] == 2009]
# df_sample = df2['date'].count()

# print(df_sample)

# # print(df2)

plt.style.use('default')
plt.rcParams['figure.figsize'] = (4,3)
plt.rcParams['font.size'] = 12

fig, ax = plt.subplots()
df =  np.arange(2009,2021)
# ax.set_ylabel('발전소 개수', color='green')
# ax.set_xlabel('연도', color='red')

ax.bar(df, kkk, color = 'green')

# #print(a)

plt.show()



# fin['datetime'] = fin['date'].apply(lambda x: pd.to_datetime(str(x), format = '%Y%m'))
# fin.set_index(fin['datetime'], inplace=True)
# fin = fin.drop('datetime', axis = 1)
# fin = fin.sort_index()

# fin['month'] = fin.index.month
# fin['year'] = fin.index.year

