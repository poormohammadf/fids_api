import requests
import json
import pymssql
#import psycopg2
requests.packages.urllib3.disable_warnings() 

server = 'localhost'
database = 'fids' 
username = 'fids_user' 
password = '1234'
conn = pymssql.connect(host=server, user=username, password=password, database=database)

cursor = conn.cursor()

airline = 'tbn'
url = 'https://ais.airport.ir/NetForm/Service/fids'

total = 0
for day in range(1, 16):
    date = f'1402-01-{"0" + str(day)}' if day < 10 else f'1402-01-{str(day)}'
    param = {
        'date' : date,
        'airline':airline,
        'AUTH_TOKEN':9890071
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate'
    }
    response = requests.get(url,params=param, headers=headers, verify=False)
    response_text = response.content.decode('utf-8')
    data = json.loads(response.text)
    flights = data['Flights']
    subtotal = 0
    for item in flights:
        origin = item['origin_icao']
        destination = item['destination_icao']
        register = item['register']
        flight_num = item['flight_num']
        airplane = item['airplane_type']
        airline_icao = item['airline_icao']
        dow = item['dow']
        status_ = item['status1']
        status1_ = item['status2']
        status2_ = item['second_status']
        type_ = item['type_']
        delay_ = 0 if item['delay'] == 'NULL' else item['delay']
        international = 0 if item['international']== "false" else 1
        scheduled_date = item['scheduled_date']
        scheduled_time = item['scheduled_time']
        actual_date = item['actual_date']
        actual_time = item['actual_time']
        miladi_scheduled = item['miladi_scheduled']
        miladi_actual = item['miladi_actual']
        vals = (origin,destination,register,flight_num,airplane,airline.upper(),airline_icao,dow,status_,status1_,status2_,type_,delay_,international,scheduled_date,scheduled_time,actual_date,actual_time,miladi_scheduled,miladi_actual)
        sql = """ insert into fids (origin,destination,register,flight_num,airplane,airline,airline_icao,dow,status_,status1_,status2_,type_,delay_,international,scheduled_date,scheduled_time,actual_date,actual_time,miladi_scheduled,miladi_actual)
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s,%s,%s,%s,%s,%s,%s); """
        try:
            cursor.execute(sql,vals)
            subtotal += 1
            conn.commit()
        except pymssql.Error as error:
            print(error)
    total += subtotal
    print(date,subtotal)
cursor.close()
print('Total:',total)
