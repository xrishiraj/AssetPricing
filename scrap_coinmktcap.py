import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/currencies/xrp/historical-data/?start=20130429&end=20200906'
content = requests.get(url).content
soup = BeautifulSoup(content, 'html.parser')
table = soup.find('table', {'class': 'table'})

data = [[td.text.strip() for td in tr.findChildrem('td')]
        for tr in table.findChildren('tr')]

df = pd.DataFrame(data)
df.drop(df.index[0], inplace=True)
df[0] = pd.to_datetime(df[0])
for i in range(1, 7):
    df[i] = pd.to_numeric(df[i].str.replace(",", "").str.replace("-", ""))
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'MarketCap']
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)
