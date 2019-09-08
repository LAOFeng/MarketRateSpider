import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

class SwapRate():
    def __init__(self):
        self.url = 'https://seb.se/pow/apps/swaprates/default.aspx'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content,'lxml')
        self.table = self.soup.find_all('table')[9]
        self.head = self.gethead()
        self.data = self.getdata()


    def gethead(self):
        head = []
        th = self.table.find_all('th')
        for each in th:
            head.append(each.text.strip())
        return head
    
    def getdata(self):
        maturity = []
        swap = []
        date = []
        tr = self.table.tbody
        for each in tr:
            if each == '\n':
                next
            else:
                maturity.append(each.find('td',class_="first").text.strip())
                swap.append(each.find('td',class_="value-cell").text.strip())
                date.append(each.find('td',class_="value-cell last").text.strip())
        print(maturity,swap,date)
        dic1={self.head[0]:maturity, self.head[1]:swap, self.head[4]:date}
        df = pd.DataFrame(dic1)
        return df

class Libor():
    def __init__(self):
        url = 'https://www.global-rates.com/interest-rates/libor/american-dollar/american-dollar.aspx'
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.content,'lxml')
        self.head = self.gethead()
        self.data = self.getdata()


    def gethead(self):
        head=['USD LIBOR']
        head.append(self.soup.find('span',attrs={"id":'lbl_hdr2'}).text.strip())
        return head
    
    def getdata(self):
        maturity=[]
        libor=[]
        #head
        tr = self.soup.find_all(name="tr",attrs={"class":re.compile(r'tabledata[1-2]')})
        for each in tr:
            maturity.append(each.find_all('td')[0].text.strip())
            libor.append(each.find_all('td')[1].text.strip().replace('\xa0',''))
        print(maturity,libor)
        dic2 = {self.head[0]:maturity, self.head[1]:libor}
        df2 = pd.DataFrame(dic2)
        return df2





Swap_Rate = SwapRate()
Libor_Rate = Libor()
print(Libor_Rate.data)
print(Swap_Rate.data)