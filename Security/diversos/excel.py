import pandas as pd

carros = {
    'marca' : ['Fiat', 'Chevrolet', 'Ford'],
    'modelo' : ['Mille', 'Celta', 'Ka'],
    'ano' : ['2011', '2013', '2010'],
}

dataframe = pd.DataFrame(carros)
dataframe.to_excel('./carros.xlsx')