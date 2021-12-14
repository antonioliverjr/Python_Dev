from clientes import BaseDeDados

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'João')

# bd._dados = 'Uma outra coisa' (Não acessar chave protected)

# bd.apaga_cliente(2)
bd.lista_clientes()