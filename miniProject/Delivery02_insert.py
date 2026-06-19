import oracledb
import requests, json

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'

conn = oracledb.connect (
    user='education',
    password='1234',
    host=host_name,
    port=oracle_port,
    service_name=service_name  
)

cursor = conn.cursor()

url = 'https://openapi.gg.go.kr/GGEXPSDLV'
params = dict(
    Type= 'json',
    psize= '10', 
    KEY= '46bc1bab66da48d09803ee84b4a75ec1'
)

raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)

for jd in json_data['GGEXPSDLV'][1]['row']:
    SIGUN_NM = jd['SIGUN_NM'] # 시군명
    STR_NM = jd['STR_NM'] # 매장명
    REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR'] # 주소
    REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']   # 위도
    REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT'] # 경도 
   
    
    sql = """insert into delivery_apps (idx, sigun, str, addr,
                latitude, longitude)
          values (seq_board_num.nextval, :sigun, :str, :addr,
                :latitude, :longitude)"""
    try:
        cursor.execute(sql, sigun=SIGUN_NM, str=STR_NM,
                   addr=REFINE_LOTNO_ADDR,
                   latitude=REFINE_WGS84_LAT,
                   longitude=REFINE_WGS84_LOGT)
        conn.commit()
        print("1개의 레코드 입력")
    except Exception as e:
         conn.rollback()
         print("insert 실행시 오류발생", e)
conn.close()
    
    
    
    
    
    
    