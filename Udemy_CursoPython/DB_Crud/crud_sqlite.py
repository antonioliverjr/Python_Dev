import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

        self.cursor.execute('create table if not exists agenda('
                            'id integer primary key autoincrement,'
                            'nome text,'
                            'telefone text'
                            ')')
        self.conn.commit()

    def inserir(self, nome, telefone):
        dados = {'nome': nome, 'telefone': telefone}
        sql = 'insert or ignore into agenda (nome, telefone)' \
              'values(:nome, :telefone)'
        self.cursor.execute(sql, dados)
        self.conn.commit()

    def editar(self, nome, telefone, id):
        dados = {'nome': nome, 'telefone': telefone, 'id': str(id)}
        sql = 'update or ignore agenda set nome = :nome, telefone = :telefone where id = :id'
        self.cursor.execute(sql, dados)
        self.conn.commit()

    def excluir(self, id):
        dados = {'id': id}
        sql = 'delete from agenda where id = :id'
        self.cursor.execute(sql, dados)
        self.conn.commit()

    def listar(self):
        self.cursor.execute('select * from agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.listar()
    #agenda.inserir('Francisca', '7199999999')
    #agenda.excluir(3)
