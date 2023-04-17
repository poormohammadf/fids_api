import requests
import json

requests.packages.urllib3.disable_warnings()

airline = 'kru'
url = 'https://ais.airport.ir/NetForm/Service/fids?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate'
}

for day in range(1, 11):
    date = f'1402-01-{day:02}'
    params = {'date': date, 'airline': airline, 'AUTH_TOKEN': '9890071'}
    
    response = requests.get(url, params=params, headers=headers, verify=False)
    data = json.loads(response.text)
    
    print(f'Data for {date}:')
    print(data)
