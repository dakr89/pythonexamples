import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib

start = datetime.datetime(2000,1,1)
end = datetime.datetime(2016,12,31)
df = web.DataReader('TSLA','yahoo',start,end)
# df['Adj Close'].plot(color='red')

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)

plt.show()