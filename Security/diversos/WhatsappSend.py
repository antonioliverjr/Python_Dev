import datetime

import pywhatkit.whats as whats
import time

hora = datetime.datetime.now().strftime('%H')
minuto = datetime.datetime.now().strftime('%M')

telDestino = "+" + input("Informe o numero de destino Exemplo: 557199999999: ")
mensagem = "Envio de teste com Python, depois de algumas tentativas com C#..."

print(telDestino, mensagem, hora, minuto)

whats.sendwhatmsg(str(telDestino), str(mensagem), int(hora), int(minuto))