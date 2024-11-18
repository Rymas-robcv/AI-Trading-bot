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

sp500["Symbol"] = sp500["symbol"].str.replace(".","-")

