import requests
from bs4 import BeautifulSoup

url='http://localhost/myproject/index.php'

r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
file = open("testfile2.txt",'w')
for el in soup.find_all('table', attrs={'border': '1' ,'style':'border-collapse:collapse;border:none;font-size:12pt;'}):
    file.write(el.get_text())

file.close()

