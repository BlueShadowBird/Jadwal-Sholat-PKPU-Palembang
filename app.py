import requests
from bs4 import BeautifulSoup

url = 'http://www.jadwalsholat.pkpu.or.id/?id=178';
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

data = soup.find_all('tr', 'table_highlight')[0]

jadwal_shalat = {}
i=0
for d in data:
    if i == 1:
        jadwal_shalat['subuh'] = d.get_text()
    elif i == 2:
        jadwal_shalat['zuhur'] = d.get_text()
    elif i == 3:
        jadwal_shalat['ashar'] = d.get_text()
    elif i == 4:
        jadwal_shalat['maghrib'] = d.get_text()
    elif i == 5:
        jadwal_shalat['isyah'] = d.get_text()
    i+=1

print(jadwal_shalat)
print(jadwal_shalat['isyah'])