import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  
import matplotlib as mpl 
from matplotlib import font_manager, rc

fin = pd.read_excel('c:/dd/fan.xlsx')

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.style.use('default')
plt.rcParams['figure.figsize'] = (4,3)
plt.rcParams['font.size'] = 12

fig, ax = plt.subplots()

# xd = pd.Series(fin)
# yr = xd.apply(lambda x: fin.iloc[2558:2922,10] < 7)


#x = fin.drop(fin.loc[fin['cloud'] >= 7].index)

ax.plot(fin.iloc[2139:2392,3], fin.iloc[2139:2392,13],color='#c02ad1') ## 선그래프 생성



ax2 = ax.twinx()

ax2.set_ylabel('발전량', color = 'green')
ax2.plot(fin.iloc[2139:2392,3], fin.iloc[2139:2392,14], color='red')

ax2.tick_params(axis='y', labelcolor='green')


plt.show()


