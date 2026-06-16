from numpy import size
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

col_years = list(map(str, range(1970, 2018)))
df4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years] 

# 데이터프레임을 전치해서 행과 열을 교환 
df4 = df4.transpose()
plt.style.use('ggplot') 
# 데이터프레임의 인덱스를 정수형으로 변경. map 함수의 첫번째 인수로
# int 함수 사용. 
df4.index = df4.index.map(int)

'''
면적그래프
  kind='area' : 면적그래프를 그리기 위한 옵션
  stacked : 그래프를 겹쳐서 표현할지 여부를 결정
  alpha : 투명도 설정. 0~1사이로 표현하고, 0에 가까울수록
      투명하게 표현된다.
'''
# False 인 경우 그래프를 겹쳐서 표현
df4.plot(kind='area', stacked=False, alpha=0.2, figsize=(20,10))
# 겹치지 않게 표현
# df4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20,10))


# 제목, 타이틀 등
plt.title('서울 -> 타시도 인구 이동', size=30)  
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간', size=20) 
plt.legend(loc='best', fontsize=15)

plt.show()  
