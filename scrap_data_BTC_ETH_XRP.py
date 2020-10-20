# This code scrapes data from coinmarketcap.com, the only website where I could find historical data for all three
# cryptocurrencies. Data had to be scraped because coindesk.com is only giving 1 year data and that to without volume
# and marketcap.


import pandas as pd
import requests

# Feeding URL
url_btc = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130429&end=20200906'
url_eth = 'https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20130429&end=20200906'
url_xrp = 'https://coinmarketcap.com/currencies/xrp/historical-data/?start=20130429&end=20200906'


# Creating requests for each URL
btc = requests.get(url_btc)
eth = requests.get(url_eth)
xrp = requests.get(url_xrp)


# Parsing each html and converting it into a list object
df_list_btc = pd.read_html(btc.text)
df_list_eth = pd.read_html(eth.text)
df_list_xrp = pd.read_html(xrp.text)


# Subsetting each list to get the OHLC data
df_btc = df_list_btc[2]
df_eth = df_list_eth[2]
df_xrp = df_list_xrp[2]


# Exporting data as in csv format
df_btc.to_csv('BTC_29Apr2013_09-05-2020.csv', index=False, header=True)
df_eth.to_csv('ETH_07Aug2015_09-05-2020.csv', index=False, header=True)
df_xrp.to_csv('XRP_04Aug2013_09-05-2020.csv', index=False, header=True)