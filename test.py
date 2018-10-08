from datetime import date
import numpy as np
from nsepy import get_history
infy = get_history(symbol='INFY',
                   start=date(2015,1,1),
                   end=date(2015,12,31))
tcs = get_history(symbol='TCS',
                   start=date(2015,1,1),
                   end=date(2015,12,31))
nifty_it = get_history(symbol="NIFTYIT",
                            start=date(2015,1,1),
                            end=date(2015,12,31),
                            index=True)
infy["4 Week"] = np.round(infy["Close"].rolling(window = 20, center = False).mean(), 2)
infy["16 Week"] = np.round(infy["Close"].rolling(window = 80, center = False).mean(), 2)
infy["32 Week"] = np.round(infy["Close"].rolling(window = 160, center = False).mean(), 2)
infy["52 Week"] = np.round(infy["Close"].rolling(window = 200, center = False).mean(), 2)
tcs["4 Week"] = np.round(tcs["Close"].rolling(window = 20, center = False).mean(), 2)
tcs["16 Week"] = np.round(tcs["Close"].rolling(window = 80, center = False).mean(), 2)
tcs["32 Week"] = np.round(tcs["Close"].rolling(window = 160, center = False).mean(), 2)
tcs["52 Week"] = np.round(tcs["Close"].rolling(window = 200, center = False).mean(), 2)
nifty_it["4 Week"] = np.round(nifty_it["Close"].rolling(window = 20, center = False).mean(), 2)
nifty_it["16 Week"] = np.round(nifty_it["Close"].rolling(window = 80, center = False).mean(), 2)
nifty_it["32 Week"] = np.round(nifty_it["Close"].rolling(window = 160, center = False).mean(), 2)
nifty_it["52 Week"] = np.round(nifty_it["Close"].rolling(window = 200, center = False).mean(), 2)
infy
infy_1 = get_history(symbol='INFY',
                   start=date(2014,12,31),
                   end=date(2015,12,30))
import pandas as pd
Vol=infy['Volume'].reset_index(drop=True)-infy_1['Volume'].reset_index(drop=True)
direction=[]
shock=[]
for Vol1 in Vol:
    if Vol1 < 0:
        direction.append(0)
    else:
        direction.append(1)
div=abs(Vol)/infy_1['Volume'].reset_index(drop=True)
for div1 in div:
    if div1 >.10:
        shock.append(1)
    else:
        shock.append(0)
shock_vol=pd.DataFrame({'shock':shock,'direction':direction},index=infy.index)
clp=infy['Close'].reset_index(drop=True)-infy_1['Close'].reset_index(drop=True)
direction=[]
shock=[]
for Vol1 in clp:
    if Vol1 < 0:
        direction.append(1)
    else:
        direction.append(0)
div=abs(clp)/infy['Close'].reset_index(drop=True)
for div1 in div:
    if div1 >.02:
        shock.append(1)
    else:
        shock.append(0)
shock_pr=pd.DataFrame({'shock':shock,'direction':direction},index=infy.index)
shock_pr
sck=shock_pr['shock'] &  ~shock_vol['shock']
pswvs=pd.DataFrame({'shock':sck,'direction':direction},index=infy.index)
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
def datetime(x):
    return np.array(x, dtype=np.datetime64)
p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'
p1.line(datetime(infy.index), infy['Close'], color='blue', legend='INFY')
p1.line(datetime(infy.index), shock_vol.shock, color='Red', legend='Vol Shock')
p1.legend.location = "top_left"

output_file("stocks.html", title="stocks.py")
show(gridplot([[p1]], plot_width=400, plot_height=400))
