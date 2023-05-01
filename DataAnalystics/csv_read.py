import pandas as pd


municipio = pd.read_csv("C:\\municipio\\municipio.csv")

df = municipio.query('ano == 2020')

df.to_csv("C:\\municipio\\municipio_2020.csv", sep="|")