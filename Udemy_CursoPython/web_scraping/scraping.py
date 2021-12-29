import requests
from bs4 import BeautifulSoup


url = r'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    for titulo in pergunta.select_one('.question-hyperlink'):
        print(titulo)
