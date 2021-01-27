from bs4 import BeautifulSoup
import requests
url = 'http://www.cntour.cn/'

str_html = requests.get(url=url).content
soup = BeautifulSoup(str_html, 'lxml')
print(soup)
 