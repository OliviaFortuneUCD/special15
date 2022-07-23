#To predict the stock prices of Netflix with machine learning,
#I will be using the LSTM neural network as it is one of the best approaches for regression analysis and time series forecasting. So here,
#I will start by importing the necessary Python libraries and collecting the latest stock price data of Netflix:

#Stock prediction

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=5000)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('NFLX',
                      start=start_date,
                      end=end_date,
                      progress=False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.tail())