import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv("Google+Trends+Data+Viz+(start)\TESLA Search Trend vs Price.csv")
df_desemprego = pd.read_csv("Google+Trends+Data+Viz+(start)\\UE Benefits Search vs UE Rate 2004-20.csv")
btc_price = pd.read_csv("Google+Trends+Data+Viz+(start)\Daily Bitcoin Price.csv")
btc_search = pd.read_csv("Google+Trends+Data+Viz+(start)\Bitcoin Search Trend.csv")

# print(df_desemprego.info())
# print(df_tesla.describe())
# print(btc_price.describe())
# print(btc_search.describe())

#DATA EXPLORATION
# max_value_tesla = df_tesla["TSLA_USD_CLOSE"].max()
# min_value_tesla = df_tesla["TSLA_USD_CLOSE"].min()
# max_value_des = df_desemprego["UE_BENEFITS_WEB_SEARCH"].max()
# print(f'Largest value for Tesla in Web Search: ', max_value_tesla)
# print(f'Smallest value for Tesla in Web Search: ', min_value_tesla) 
# print('Largest value for "Unemployemnt Benefits" Web Search: ', max_value_des)
# What does a value of 100 in the Google Trend search popularity actually mean?
# The Google Trends data is normalized to a scale of 0 to 100, where 100 is the maximun value
# print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
# print(f'Missing values for U/E?: {df_desemprego.isna().values.any()}')
# print(f'Missing values for BTC Search?: {btc_search.isna().values.any()}')
# print(f'Missing values for BTC Search?: {btc_price.isna().values.any()}')
# print(f'Missing values for BTC Search?: {btc_price.isna().values.any().sum()}')
# Only one value, so it's better just drop this index

#DATA CLEANING
# Removing the index with no value
btc_price.dropna(inplace=True)

# # Converting Strings to DateTime Objects
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_desemprego.MONTH = pd.to_datetime(df_desemprego.MONTH)
btc_search.MONTH = pd.to_datetime(btc_search.MONTH)
btc_price.DATE = pd.to_datetime(btc_price.DATE)
# print(df_desemprego.info()) #Confirming the new type
# DATE
df_btc_monthly = btc_price.resample('ME', on='DATE').last()

#DATA VISUALIZATION
# Plotting the data of TESLA and Serach of TESLA
plt.figure(figsize=(14,8), dpi=120) 
plt.title('Tesla Web Search vs Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
plt.show()

# Plotting the data of BITCOIN and Serach of BITCOIN
plt.figure(figsize=(14,8), dpi=120) 
plt.title('Bitcoin News Search vs Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('BTC PRICE', color='#E6232E', fontsize=14)
ax2.set_ylabel('BTC NEWS SEARCH', color='skyblue', fontsize=14)
 
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, btc_search.BTC_NEWS_SEARCH, color='skyblue', linewidth=3, marker='o')
plt.show()

# Plotting the data of Unemployment and Serach of Unemployment
plt.figure(figsize=(14,8), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
 
ax1.set_xlim([df_desemprego.MONTH.min(), df_desemprego.MONTH.max()])
 
ax1.plot(df_desemprego.MONTH, df_desemprego.UNRATE, 'purple', linewidth=3)
ax2.plot(df_desemprego.MONTH, df_desemprego.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
plt.show()