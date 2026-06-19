import oracledb
import folium

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

sigun = input('시군명을 입력하세요 : ')

delivery_apps_map = folium.Map(location=[37.40,127.38],zoom_start=12)

sql = """select * from delivery_apps where sigun = :1 order by idx asc fetch first 10 rows only"""
cursor.execute(sql, [sigun])

for rs in cursor:
    idx = rs[0]
    db_sigun = rs[1] 
    str = rs[2]
    addr = rs[3]  
    latitude = rs[4]  
    longtitude = rs[5]  
    
    if latitude is None or longtitude is None:
        continue
    
    folium.Marker([latitude,longtitude],
                  popup=str).add_to(delivery_apps_map)
    print(str, latitude, longtitude)
    
delivery_apps_map.save('../saveFiles/delivery_apps_map_{sigun}.html')
print("맵이 생성되었습니다.")
    