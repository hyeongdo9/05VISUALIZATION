import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0) 

df = df.ffill() 
print(df.head())
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul =df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)  
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

col_years = list(map(str, range(2010, 2018)))
df4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years] 

# 앞에서 적용한 연도 사이에 이동한 인구수를 각 도별로 합산하여 새로운 열 추가  
df4['합계'] = df4.sum(axis=1)
# print(df4)
# 새롭게 생성한 '합계' 열을 오름차순으로 정렬하여 변수에 저장 
df_total = df4[['합계']].sort_values(by='합계', ascending=True)
plt.style.use('ggplot')
# 수평방향의 막대그래프를 생성
df_total.plot(kind='barh', color='cornflowerblue', width=0.5, figsize=(10,5))


plt.title('서울 -> 타시도 인구 이동')  
plt.ylabel('전입지')
plt.xlabel('이동 인구 수') 

plt.show()  
