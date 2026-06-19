from ctypes.wintypes import PSIZE

import requests, json

url = 'https://openapi.gg.go.kr/GGEXPSDLV'
params = dict(
    Type= 'json',
    psize= '10', 
    KEY= '46bc1bab66da48d09803ee84b4a75ec1'
)
raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)
print(json_data)

for jd in json_data['GGEXPSDLV'][1]['row']:

    SIGUN_NM = jd['SIGUN_NM'] # 시군명
    STR_NM = jd['STR_NM'] # 매장명
    REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR'] # 주소
    REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']   # 위도
    REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT'] # 경도 
    print(STR_NM, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)
