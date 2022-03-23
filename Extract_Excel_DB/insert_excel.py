import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine("mssql+pyodbc://project:Jrdbsql@localhost\\SQLEXPRESS/PANDAS?driver=ODBC+Driver+17+for+SQL+Server")

metadata_obj = MetaData()

municipios = Table(
    'municipios',
    metadata_obj,
    Column('ano', Integer),
    Column('id_municipio', Integer),
    Column('sexo', String(20)),
    Column('grupo_idade', String(20)),
    Column('populacao', Integer)
)

metadata_obj.create_all(engine, checkfirst=True)

df = pd.read_csv('C:\municipio\municipio.csv', sep=',', header=0)
df = df.head(10000)
df.to_sql('municipios', con=engine, if_exists='replace', index=False, chunksize=1000000)

with engine.connect() as conn:
    result = conn.execute(municipios.select().limit(100))
    data = [data for data in result]

df2 = pd.DataFrame(data, columns=['ano', 'id_municipio', 'sexo', 'grupo_idade', 'populacao'])
print(df2)