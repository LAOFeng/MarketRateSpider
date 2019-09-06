import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://seb.se/pow/apps/swaprates/default.aspx'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
table = soup.find_all('table')[9]
th = table.find_all('th')
tr = table.tbody
head = []
for each in th:
    head.append(each.text.strip())
print(head)

maturity = []
swap = []
date = []

for each in tr:
    if each == '\n':
        next
    else:
        maturity.append(each.find('td',class_="first").text.strip())
        swap.append(each.find('td',class_="value-cell").text.strip())
        date.append(each.find('td',class_="value-cell last").text.strip())
print(maturity,swap,date)

dic1={head[0]:maturity, head[1]:swap, head[4]:date}
df = pd.DataFrame(dic1)
print(df)
