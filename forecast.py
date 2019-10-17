import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage


response = requests.get('https://www.aladin.info/sr/bosna-i-hercegovina/brcko-dugorocna-prognoza-vremena')

soup = BeautifulSoup(response.text, 'lxml')
tomorrow = soup.find_all('li', class_='font_150_rem text-primary')[2]
string = tomorrow.text
sliced_string = string.split("°", 1)
temperature = sliced_string[0]

mail_user = os.environ.get('my_email')
pass_user = os.environ.get('my_email_pass')

msg = EmailMessage()
msg['Subject'] = 'Vremenska prognoza'
msg['From'] = mail_user
msg['To'] = [mail_user]
msg.set_content("Ova poruka je automatski generisan izvjestaj!\n\n\
Prognozirana temperatura za sutra ujutro je {} stepeni Celzijusa.\n\n\
Pripremite jakne.".format(temperature))

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(mail_user, pass_user)
    
    server.send_message(
            msg
    )

    server.quit()
    

if int(temperature) <= 10:
    send_mail()