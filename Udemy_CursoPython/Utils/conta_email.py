import os
import shutil
from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

caminho_imagem = r'C:\Users\antoliverjr\Pictures'
caminho_destino = r'img'

if not os.path.exists(caminho_destino):
    os.mkdir(caminho_destino)

for files in os.listdir(caminho_imagem):
    if 'Python' in files:
        caminho_origem = caminho_imagem + '\\' + files
        caminho_destino = caminho_destino + '\\' + files
        shutil.copy(caminho_origem, caminho_destino)

with open('template.html', 'r', encoding='UTF-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Antonio Oliveira', data=data_atual)


email = '##############@gmail.com'
senha = '##########'

msg = MIMEMultipart()
msg['from'] = 'Antonio Oliveira'
msg['to'] = '#############@gmail.com'
msg['subject'] = 'Atenção - Email de teste em Python ;)'

with open(caminho_destino, 'rb') as image:
    image = MIMEImage(image.read())
    msg.attach(image)

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as gmail:
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email, senha)
    gmail.send_message(msg)
    print('E-mail enviado com sucesso')






