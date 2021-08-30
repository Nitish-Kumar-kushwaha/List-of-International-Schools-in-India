import csv
from googlesearch import search
import requests
from bs4 import BeautifulSoup

url = "https://www.internationalschoolsearch.com/search/All+All+All+India+All/"

datas = []

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

items= soup.findAll('div', 'col-md-4 listing')
# print(items)

for x in items:
    names = x.findAll('h3')
    actualNames = names[1].string
    #     print(names[1].string)

    address = x.findAll('p')
    actual = address[0].text
    ActualAdress = actual.strip('\n')
    ActualAdress = ActualAdress.strip('\t')
    string = str(actualNames) + str(ActualAdress)
    j = search(string, num_results=3)
    # print(j[0])
    datas.append([actualNames, ActualAdress,j[0]])
    # print(actual)

    # list = pd.DataFrame({'names':names, 'actual':actual})

with open('international.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    headers = ['Schools Names',' Schools Address', 'websites']
    writer.writerow(headers)
    for data in datas:
        writer.writerow(data)
#
# print("Stopped")