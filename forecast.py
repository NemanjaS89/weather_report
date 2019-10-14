import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.aladin.info/sr/bosna-i-hercegovina/brcko-dugorocna-prognoza-vremena')

status = response.status_code
soup = BeautifulSoup(response.text, 'lxml')

tomorrow = soup.find_all('li', class_='font_150_rem text-primary')[2]

print(status)
print(tomorrow.text)