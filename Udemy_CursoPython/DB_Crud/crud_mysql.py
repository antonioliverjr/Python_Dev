import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    context = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Jrdbsql86',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield context
    finally:
        context.close()

# cursor = context.cursor()
# cursor.execute('create table if not exists clientes('
#                'id INT not null auto_increment primary key,'
#                'nome varchar(255) null,'
#                'sobrenome varchar(255) null,'
#                'idade INT(11) not null,'
#                'peso float null'
#                ')')
# cursor.execute("insert into clientes (nome, sobrenome, idade, peso)"
#                "values ('Luiz', 'Otávio', 20, 100), ('Antonio', 'Oliveira', 35, 113), ('Joana', 'Silva', 32, 78),"
#                "('Roberto', 'Oliveira', 27, 80), ('Fabrício', 'Felix', 35, 99)")
# context.commit()


# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'insert into clientes (nome, sobrenome, idade, peso) values' \
#               '(%s, %s, %s, %s)'
#         dados = ('Ana', 'Cecilia', 9, 55)
#         cursor.execute(sql, dados)
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'insert into clientes (nome, sobrenome, idade, peso) values' \
#               '(%s, %s, %s, %s)'
#         dados = [
#             ('Ana', 'Cecilia', 9, 55),
#             ('Cassia', 'Oliveira', 29, 100),
#             ('Ane', 'Oliveira', 39, 79),
#             ('Maria', 'Jose', 25, 80)
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()


# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'delete from clientes where id = %s'
#         dados = (7)
#         cursor.execute(sql, dados)
#         conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'update clientes set nome = %s, sobrenome = %s, idade = %s, peso = %s where id = %s'
        dados = ('Ana Cecilia', 'Oliveira', 9, 65, 6)
        cursor.execute(sql, dados)
        conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('select * from clientes')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)

