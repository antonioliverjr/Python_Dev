from mysql import connector

class Context:
    def __init__(self) -> None:
        self.__db = connector.connect(
            host='127.0.0.1',
            user='root',
            password='Jrdbsql86',
            database='movies_controll'
        )
    
    def conn(self):
        return self.__db

    def commit(self):
        self.__db.commit()
    
    def close(self):
        self.__db.close()
