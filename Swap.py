import requests
from bs4 import BeautifulSoup
import pandas as pd

class SwapRate():
    def __init__(self):
        url = 'https://seb.se/pow/apps/swaprates/default.aspx'
        self.response = requests.get(url)
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


Swap_Rate = SwapRate()

print(Swap_Rate.data)