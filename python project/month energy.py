import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_excel('c:/dd/한국남동발전_발전실적 (1).xlsx')
df.columns = ['loc', 'plant', 'date', 'storage', 'EG', 'ther', 'userate', 'generator']
df = df[df['generator'] == '태양력']
# Datetime Index 설정
df['datetime'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format = '%Y%m'))
df.set_index(df['datetime'], inplace=True)
df = df.drop('datetime', axis = 1)
df = df.sort_index()
# 피벗 테이블 생성
df['month'] = df.index.month
df['year'] = df.index.year
df2 = df[['EG', 'month', 'year']].copy()
pivot = pd.pivot_table(df2, index = ['month'], columns = ['year'])
# 계절성 그래프
pivot.plot()
plt.xticks(range(1, 13))
plt.ylabel('Electricity Generation')
plt.title('Seasonal Plot')
plt.show()