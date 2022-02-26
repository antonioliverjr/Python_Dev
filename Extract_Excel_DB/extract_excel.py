import pyodbc
import pandas as pd

context = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=AGENDA;UID=project;PWD=Jrdbsql'
)

cursor = context.cursor()
cursor.execute('select Id, Nome, Sobrenome from contatos')

resultado = cursor.fetchall()
print(resultado)
#for result in resultado:
#    print(result)

df = pd.DataFrame.from_records(resultado, columns=['Id','Nome','Sobrenome'])
df.to_excel("contatos.xlsx", sheet_name='lista1')

cursor.close()
context.close()