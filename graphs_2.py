import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

y_symbols = ['TSLA', 'GOOGL', 'AAPL', 'NIO']
startdate = '2019-01-01'
enddate = '2023-01-01'

data = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)['Adj Close']

returns = data.pct_change()        
log_returns = np.log(1+data.pct_change())

sns.histplot(log_returns)
plt.xlabel("Daily Returns")
plt.ylabel("Frequency")
plt.show()