# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 22:46:16 2014

@author: raghu
"""

import pandas as pd
from datetime import datetime
from datetime import *
from pandas.io.data import DataReader
#TECHM.NS,HCLTECH.NS

#axis = DataReader("AXISBANK.NS","yahoo",datetime(2013,3,1),datetime(2014,3,31))
nifty = DataReader("^NSEI","yahoo",datetime(2013,5,1),datetime(2013,5,25))
bn=DataReader("^NSEBANK","yahoo",datetime(2013,5,1),datetime(2013,5,25))
#print spx.head()
#print ss0.head()

#print axis.tail()
print nifty.tail()['Close'],bn.tail()['Close']
print nifty.head()['Close'],bn.head()['Close']

#axis_daily= axis.tail().diff()['Close']
#nifty_daily=nifty.tail().diff()['Close']
#axis_daily= axis.diff()['Close']
nifty_daily=nifty.diff()['Close']
bn_daily=bn.diff()['Close']
#daily_return = (axis_daily*250 ) - (50*nifty_daily)
daily_return = (bn_daily*25)- (50*nifty_daily)
nifty_daily_return =50*(nifty_daily)
bn_daily_return =25*(bn_daily)

print -nifty_daily_return.sum()+bn_daily_return.sum()

both = pd.DataFrame(data = {'nifty': 50*nifty.diff()['Adj Close'], 'bn': 25*bn.diff()['Adj Close']})
print both.plot()

current = datetime.datetime.now
print current
current =+datetime.timedelta(days=1)
print current

