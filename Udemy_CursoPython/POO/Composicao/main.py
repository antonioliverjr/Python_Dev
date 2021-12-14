from classes import Cliente

antonio = Cliente('Antonio', 35)
antonio.insere_endereco('Camaçari', 'BA')
antonio.insere_endereco('Lauro de Freitas', 'BA')

cassia = Cliente('Cassia', 29)
cassia.insere_endereco('Camaçari', 'BA')

cecilia = Cliente('Ana Cecília', 9)
cecilia.insere_endereco('Camaçari', 'BA')

print(antonio.nome)
antonio.lista_enderecos()
print(cassia.nome)
cassia.lista_enderecos()
print(cecilia.nome)
cecilia.lista_enderecos()
