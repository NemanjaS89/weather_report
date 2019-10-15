import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.aladin.info/sr/bosna-i-hercegovina/brcko-dugorocna-prognoza-vremena')

soup = BeautifulSoup(response.text, 'lxml')
tomorrow = soup.find_all('li', class_='font_150_rem text-primary')[2]

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('simic.nemanja1989@gmail.com', '')
    
    subject = ''
    body = ''
    msg = f"Subject: {subject}\n\n{body}
    
    server.sendmail(
            'simic.nemanja1989@gmail.com'
            ''
            ''
            msg
    )