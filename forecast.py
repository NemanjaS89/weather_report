import os
import requests
from bs4 import BeautifulSoup
import smtplib


response = requests.get('https://www.aladin.info/sr/bosna-i-hercegovina/brcko-dugorocna-prognoza-vremena')

soup = BeautifulSoup(response.text, 'lxml')
tomorrow = soup.find_all('li', class_='font_150_rem text-primary')[2]
string = tomorrow.text
sliced_string = string.split("°", 1)
temperature = sliced_string[0]

mail_user = os.environ.get('my_email')
pass_user = os.environ.get('my_email_pass')

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(mail_user, pass_user)
    
    subject = 'Vremenska prognoza'
    body = 'Ova poruka je automatski generisan izvjestaj!\n\nPrognozirana temperatura za sutra ujutro je {}'.format(temperature)
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
            mail_user,
            mail_user,          
            msg
    )
    

send_mail()