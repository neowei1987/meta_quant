from binance.client import Client
import pandas as pd
import mplfinance as mpl

api_key = "Y2kKcBDco2qrE94Ik0zHsKtl7jQQGSF170sVRLkA5oVPf8KITmIro5hZRxeSAI8z"
api_secret = "FF7DzkcriUpEAQyW9v5rEsLUAMdhqIjlzYCFu3ietKJfi7SyAoDtxIEdc80Os4i8"
client=Client(api_key, api_secret)

print(client.ping())

# 获取当前tick
df = pd.DataFrame(client.get_all_tickers())
df = df.set_index("symbol")
df["price"]=df["price"].astype("float")
df.index = df.index.astype("string")
print(df)

# 获取历史数据
asset="BTCUSDT"
start="2021.10.1"
end="2021.11.1"
timeframe="1d"

df= pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
print(df)

df=df.iloc[0:6]
df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
df=df.set_index("Date")
df.index=pd.to_datetime(df.index, unit="ms")
df = df.astype("float")

mpl.plot(df, type='candle', volume=True, mav=7)

#cm_futures_client = CMFutures()

# get server time
#print(cm_futures_client.time())

#cm_futures_client = CMFutures(key=api_key, secret=api_secret)

#print(cm_futures_client.account())
