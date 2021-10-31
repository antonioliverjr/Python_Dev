from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///desenvolver.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class DbDesenvolvedor(Base):
    __tablename__='desenvolvedor'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), index=True)

    def __repr__(self):
        return '<Desenvolvedor Id: {}, Nome: {}>'.format(self.id, self.nome)

    def save(self):
        db_session.add()
        db_session.commit()

class DbHabilidade(Base):
    __tablename__='habilidade'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), index=True)

    def __repr__(self):
        return '<Habilidade Id: {}, Descrição: {}>'.format(self.id, self.descricao)

    def save(self):
        db_session.add()
        db_session.commit()

class DbDesenvolvedores(Base):
    __tablename__='desenvolvedores'
    id = Column(Integer, primary_key=True)
    desenvolvedor_id = Column(Integer, ForeignKey('desenvolvedor.id'))
    desenvolvedor = relationship("Desenvolvedor")
    habilidade_id = Column(Integer, ForeignKey('habilidade.id'))
    habilidade = relationship("Habilidade")

    def __repr__(self):
        return '<Desenvolvedor {}, com Habilidade {}>'.format(self.desenvolvedor_id, self.habilidade_id)

    def save(self):
        db_session.add()
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__=='__main__':
    init_db()