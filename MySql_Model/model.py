from typing import List, Tuple, Union
from context import Context


class Movies:
    def __execute(self, sql:str, data:Tuple = None):
        self.cont = Context()
        self.conn = self.cont.conn()
        self.cur = self.conn.cursor()
        self.sql = sql
        if data is not None:
            self.data = data
            try:
                self.cur.execute(sql, data)
                self.cont.commit()
                return True
            except:
                return False
            finally:
                self.cont.close()
        else:
            try:
                self.cur.execute(sql)
                self.result = self.cur.fetchall()
                return self.result
            except:
                return []
            finally:
                self.cont.close()

    def getList(self) -> Union[List, bool]:
        sql = "select mv.name, tp.type_name, if(mv.total_ep is null,'N/A', mv.total_ep) as total_ep, "+\
            "if(mv.atual_ep is null, 'N/A', mv.atual_ep) as atual_ep, mv.last_view "+ \
            "from movies as mv inner join types as tp on tp.id = mv.type"
        return self.__execute(sql)
