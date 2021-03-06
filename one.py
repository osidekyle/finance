import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")

start=dt.datetime(2015,1,1)
end=dt.datetime.now()

df = web.DataReader("TSLA", 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date",inplace=True)


df.to_csv("TSLA.csv")
df=pd.read_csv("tsla.csv",parse_dates=True,index_col=0)

df['100MA']=df['Adj Close'].rolling(window=100,min_periods=0).mean()


ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)


ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100MA'])
ax2.plot(df.index,df['Volume'])

plt.show()
