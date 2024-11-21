from statsmodels.regression.rolling import RollingOLS
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import pandas_ta
import warnings
warnings.filterwarnings("ignore")

sp500 = pd.read.html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

for i in range(len(sp500)):
    if "." in sp500[i]:
        sp500[i].str.replace(".","-")


symbolsList = sp500["Symbol"].unique().tolist()

end_date = "2024-11-16"
start_date = pd.to_datetime(end_date)-pd.DateOffset(365*8)
df = yf.download(tickers = symbolsList,
                 start =start_date,
                 end = end_date)
df.index.names = ['date','ricker']

df.columns = df.columns.str.Lower()
