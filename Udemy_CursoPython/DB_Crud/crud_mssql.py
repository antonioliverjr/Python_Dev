import pyodbc

context = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=CURSOS;UID=project;PWD=Jrdbsql'
)

cursor = context.cursor()
cursor.execute('select * from dbo.tb_usuarios')

resultado = cursor.fetchall()
for result in resultado:
    print(result)

cursor.close()
context.close()

