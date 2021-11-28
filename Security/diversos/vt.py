import phonenumbers

from phonenumbers import geocoder

phone = input('''
                Digite o telefone no formato 1140028922:
                País padrão é (+55), caso nº de fora, informe +111199999999 
                ''')

if(phone[0:3] != '+55' and len(phone) == 10):
    phone = '+55'+phone
    print(phone)
    phone_numbers = phonenumbers.parse(phone)
    print(phone_numbers)
else:
    print(phone)
    phone_numbers = phonenumbers.parse(phone)
    print(phone_numbers)

print(geocoder.description_for_number(phone_numbers, 'pt'))