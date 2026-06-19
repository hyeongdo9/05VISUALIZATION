import oracledb
import folium

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

# 폴리엄으로 지도 생성
univ_map = folium.Map(location=[37.40,127.38], zoom_start=10)
univ_map.save('../saveFiles/univ_map.html')

sql = "select * from g_univ order by idx asc"
cursor.execute(sql)
for rs in cursor:
    idx = rs[0]
    sigun = rs[1]
    faclt = rs[2]
    addr = rs[3]
    latitude = rs[4]  
    longitude = rs[5]
    
    folium.Marker([latitude,longitude],
                  popup=faclt).add_to(univ_map)
    print(faclt, latitude, longitude)
    
univ_map.save('../saveFiles/univ_map_marker.html')
print("맵이 생성되었습니다.")
