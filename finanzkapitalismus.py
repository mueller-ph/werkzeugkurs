import matplotlib.pyplot as plt
import pandas as pd
import pandas.io.data as web
import datetime
start = datetime.datetime(1980, 12, 12)

# get data from Yahoo for Apple from 1980-12-12 until today
stock_data = web.DataReader("AAPL", 'yahoo', start)
print stock_data.iloc[0]
print stock_data.iloc[-1]
#
# datum max('Adj Close')
tmax=stock_data['Adj Close'].idxmax()
print stock_data.ix[tmax]
# 
stock_data['rel_intraday_loss'] = (stock_data['Close']-stock_data['Open'])/stock_data['Open']
date_min = stock_data['rel_intraday_loss'].idxmin()
date_max = stock_data['rel_intraday_loss'].idxmax()
# Kursverlauf-plot
p2=stock_data['Adj Close'].plot()
plt.show()

