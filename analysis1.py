# Description: This is a python programme for cryptocurrency analysis

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns

df_btc = pd.read_csv('BTC_29Apr2013_09-05-2020.csv')
df_eth = pd.read_csv('ETH_07Aug2015_09-05-2020.csv')
df_xrp = pd.read_csv('XRP_04Aug2013_09-05-2020.csv')

# Printing first five rows of each crypto
print(df_btc.head())
print(df_eth.head())
print(df_xrp.head())

# Creating a new dataframe with daily closing prices
df = pd.DataFrame({'BTC': df_btc['Close**'],
                   'ETH': df_eth['Close**'],
                   'XRP': df_xrp['Close**']})
print(df.head())

# Prelimniary Statistical analysis
print(df.describe())

plt.style.use('fivethirtyeight')
my_crypto = df
plt.figure(figsize=(12.2, 4.5))
for c in my_crypto.columns.values:
    plt.plot(my_crypto[c], label=c)
plt.title('CryptoGraph')
plt.xlabel('Days')
plt.ylabel('Crypto Price ($)')
plt.legend(my_crypto.columns.values, loc='upper left')
plt.show()

# Scaling data as BTC is trading at a proportionally high cost
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 100))
scaled = min_max_scaler.fit_transform(df)
print(scaled)
df_scale = pd.DataFrame(scaled, columns=df.columns)

# Visualize the scaled data
my_crypto = df_scale
plt.figure(figsize=(12.4, 4.5))
for c in my_crypto.columns.values:
    plt.plot(my_crypto[c], label=c)
plt.title('Cryptocurrency Scaled Graph')
plt.xlabel('Days')
plt.ylabel('Crypto Scaled Price ($)')
plt.legend(my_crypto.columns.values, loc='upper left')
plt.show()

# Daily simple return
DSR = df.pct_change(1)
print(DSR.head())

# Cumulative Simple return
DCSR = (DSR + 1).cumprod()
print(DCSR.head())


# Visualize and graph the daily simple returns
plt.figure(figsize=(12, 4.5))
for c in DSR.columns.values:
    plt.plot(DSR.index, DSR[c], label=c, lw=2, alpha=.7)
plt.title('Daily Simple Returns')
plt.ylabel('Percentage (in decimal form')
plt.xlabel('Days')
plt.legend(DSR.columns.values, loc='upper right')
plt.show()

# Volatility, Mean and Correlation matrix
print(DSR.std())
print(DSR.mean())
print(DSR.corr())

# Cor-realtion matrix heat map
plt.subplots(figsize=(11, 11))
sns.heatmap(DSR.corr(), annot=True, fmt='.2%')

# $1 investment in these currencies
plt.figure(figsize=(12.2, 4.5))
for c in DCSR.columns.values:
    plt.plot(DCSR.index, DCSR[c], lw=2, label=c)
plt.title('Daily Cumulative Simple Return')
plt.xlabel('Days')
plt.ylabel('Growth of $1 investment')
plt.legend(DCSR.columns.values, loc='upper left', fontsize=10)
plt.show()
