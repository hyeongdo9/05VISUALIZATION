# 모듈 임포트
import oracledb
import requests, json

# 오라클 접속을 위한 기본 정보
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'

# 오라클 연결
conn = oracledb.connect (
    user='education',
    password='1234',
    host=host_name,
    port=oracle_port,
    service_name=service_name  
)
# 쿼리문 실행을 위한 커서 생성 
cursor = conn.cursor()
# OpenAPI의 요청 URL과 파라미터 준비 
url = 'https://openapi.gg.go.kr/Jnclluniv?'
params =  dict(
    Type= 'json',
    pSize='300', 
    KEY='37036b829e80435b9bd513cb9d7cdfd3')
# 요청 및 JSON데이터 가져오기
raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)
# print(json_data)

# 데이터의 갯수만큼 반복
for jd in json_data['Jnclluniv'][1]['row']: 
    SIGUN_NM = jd['SIGUN_NM'] # 시군명
    FACLT_NM = jd['FACLT_NM'] # 대학명
    REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR'] # 주소
    REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']   # 위도
    REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT'] # 경도 
    # print(FACLT_NM, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)
    
    # 인파라미터가 있는 insert 쿼리문 작성
    sql = """insert into g_univ (idx, sigun, faclt, addr,
                latitude, longitude)
          values (seq_board_num.nextval, :sigun, :faclt, :addr,
                :latitude, :longitude)"""
    try:
        # insert 처리 
        cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM,
                   addr=REFINE_LOTNO_ADDR,
                   latitude=REFINE_WGS84_LAT,
                   longitude=REFINE_WGS84_LOGT)
        conn.commit()
        print("1개의 레코드 입력")
    except Exception as e:
         conn.rollback()
         print("insert 실행시 오류발생", e)
conn.close()
                
