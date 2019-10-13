from bs4 import BeautifulSoup
from selenium import webdriver

url = ('https://www.aladin.info/sr/bosna-i-hercegovina/brcko-dugorocna-prognoza-vremena')

browser = webdriver.Chrome('resources/chromedriver.exe')

soup = BeautifulSoup(browser.page_source, 'lxml')


print(soup)