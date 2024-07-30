import pandas as pd

df_tesla = pd.read_csv("Google+Trends+Data+Viz+(start)\TESLA Search Trend vs Price.csv")
df_desemprego = pd.read_csv("Google+Trends+Data+Viz+(start)\\UE Benefits Search vs UE Rate 2004-20.csv")
btc_price = pd.read_csv("Google+Trends+Data+Viz+(start)\Daily Bitcoin Price.csv")
btc_search = pd.read_csv("Google+Trends+Data+Viz+(start)\Bitcoin Search Trend.csv")

print(df_desemprego.info())
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

# Converting Strings to DateTime Objects
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_desemprego.MONTH = pd.to_datetime(df_desemprego.MONTH)
btc_search.MONTH = pd.to_datetime(btc_search.MONTH)
btc_price.DATE = pd.to_datetime(btc_price.DATE)
print(df_desemprego.info()) #Confirming the new type
