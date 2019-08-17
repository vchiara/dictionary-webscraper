import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.bab.la/dictionary/english-spanish/hello'

response = requests.get(url)
response

data = response.text
soup = BeautifulSoup(data)

translation_list = soup.find(class_='content')

rows = translation_list.findAll(class_="quick-result-entry")
row = translation_list.find(class_="quick-result-entry")

for row in rows[:-1]:
     from_word = row.find(class_="babQuickResult").get_text(separator = ",").replace("\n","")
     to_word = row.find(class_="sense-group-results").get_text(separator = ",").replace("\n,","").replace(",\n","")
     translation = {from_word : to_word}
     print(translation)

example_list = soup.find(class_='result-block container')

rows_ex = example_list.findAll('div',{"class" : 'dict-example'})
row_ex = example_list.find('div',{"class" : 'dict-example'})

for row_ex in rows_ex:
     from_ex = row_ex.find(class_="dict-source").get_text()
     from_ex = from_ex.split('\n')[-1]
     to_ex = row_ex.find('div',{"class" : "dict-result"}).get_text()
     to_ex = " ".join(to_ex.split()).replace("expand_more ", "")
     examples = {from_ex : to_ex}
     print(examples)