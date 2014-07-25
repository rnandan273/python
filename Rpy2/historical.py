# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 00:53:17 2014

@author: raghu
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import *
from pandas.io.data import DataReader


def getLongShortPayOff(year,month,longSymbol,longQty,shortSymbol,shortQty):
    shortStk = DataReader(shortSymbol,"yahoo",datetime(year,month,1),datetime(year,month,25))
    longStk=DataReader(longSymbol,"yahoo",datetime(year,month,1),datetime(year,month,25))

    short_daily=shortStk.diff()['Close']
    long_daily=longStk.diff()['Close']

    short_daily_return =shortQty*(short_daily)
    long_daily_return =longQty*(long_daily)
    #print abs(long_daily_return.sum())-abs(short_daily_return.sum())
    return abs(long_daily_return.sum())-abs(short_daily_return.sum())
    
def getPayOff(year,month):
    nifty = DataReader("^NSEI","yahoo",datetime(year,month,1),datetime(year,month,25))
    bn=DataReader("^NSEBANK","yahoo",datetime(year,month,1),datetime(year,month,25))

    nifty_daily=nifty.diff()['Close']
    bn_daily=bn.diff()['Close']

    nifty_daily_return =50*(nifty_daily)
    bn_daily_return =25*(bn_daily)
    return -nifty_daily_return.sum()+bn_daily_return.sum()
    
def getRatioPayOff(year,month):
    nifty = DataReader("^NSEI","yahoo",datetime(year,month,1),datetime(year,month,25))
    bn=DataReader("^NSEBANK","yahoo",datetime(year,month,1),datetime(year,month,25))

    nifty_daily=nifty['Close']
    bn_daily=bn['Close']
    ratio = bn_daily/nifty_daily 
    sma = movingaverage(ratio,3)
    #print sma
    return ratio, sma

def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    #including valid will REQUIRE there to be enough datapoints.
    #for example, if you take out valid, it will start @ point one,
    #not having any prior points, so itll be 1+0+0 = 1 /3 = .3333
    smas = np.convolve(values, weigths, 'valid')
    return smas # as a numpy array
#dataset = [1,5,7,2,6,7,8,2,2,7,8,3,7,3,7,3,15,6]
#Will print out a 3MA for our dataset
#print movingaverage(dataset,3)
"""
print -nifty_daily_return.sum()+bn_daily_return.sum()

both = pd.DataFrame(data = {'nifty': 50*nifty.diff()['Adj Close'], 'bn': 25*bn.diff()['Adj Close']})
print both.plot()
"""

def resizeData(payoff):
    xx=np.resize(payoff,(4,12))
    return xx
    
def runAnalysis(longSymbol,longQty,shortSymbol,shortQty):
    print longSymbol+"-"+shortSymbol
    payoff=[]
    arr = np.arange(4)
    year = 2010+arr

    arr = np.arange(12)
    month = 1+arr
    print year
    print month
    
    for i in year:
        for j in month:
            payoff.append(getLongShortPayOff(i,j,longSymbol,longQty,shortSymbol,shortQty))


    #dfi = pd.DataFrame(resizeData(payoff),columns=['J','F','M','A','M','J','J','A','S','O','N','D'])

    #print dfi
    return payoff


def runRatioAnalysis():
    payoff=[]
    arr = np.arange(1)
    year = 2008+arr

    arr = np.arange(11)
    month = 1+arr

    for i in year:
        for j in month:
            payoff.append(getRatioPayOff(i,j))
            
    return payoff


#print getLongShortPayOff(2014,2,"AXISBANK.NS",250,"^NSEI",50)
#print getLongShortPayOff(2014,4,"TATAMOTOR.NS",1000,"^NSEI",50)
#print getLongShortPayOff(2014,4,"^NSEBANK",25,"^NSEI",50)

axisPayoff = runAnalysis("AXISBANK.NS",250,"^NSEI",50)
tmPayoff= runAnalysis("TATAMOTOR.NS",1000,"^NSEI",50)
bnpayoff = runAnalysis("^NSEBANK",25,"^NSEI",50)

both = pd.DataFrame(data = {'axis':axisPayoff, 'tm': tmPayoff,'bn': bnpayoff})
#print both.plot()
#both.plot()

# plot histograms
plt.hist(axisPayoff, bins=48, histtype='stepfilled', normed=True, color='b', label='Axis')
plt.hist(tmPayoff, bins=48, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='TM')
plt.hist(bnpayoff, bins=48, histtype='stepfilled', normed=True, color='g', alpha=0.5, label='BN')
plt.show()
print sum(axisPayoff)
print sum(tmPayoff)
print sum(bnpayoff)

current = datetime.datetime.now
print current
current =+datetime.timedelta(days=1)
print current
"""
#print getLongShortPayOff(2014,1,"TATAMOTOR.NS",1000,"^NSEI",50)
axisPayoff = runAnalysis("AXISBANK.NS",250,"^NSEI",50)
tmPayoff= runAnalysis("TATAMOTOR.NS",1000,"^NSEI",50)
tmPayoff=[-7074.9999999999927, 8012.5000000000309, -10240.000000000004, 12679.999999999967, 15399.999999999985, -6152.5000000000273, 5244.99999999996, 27454.999999999978, -14892.499999999978, 12420.000000000009, -8850.0000000000109, 1344.99999999996, 4979.9999999999782, 2647.5000000000018, 1802.5000000000164, -2272.5000000000118, 692.49999999998545, 16652.499999999996, -315.00000000001637, 15590.000000000029, -2562.5000000000055, 21095.000000000004, -5794.9999999999891, -9192.5000000000309, 27350.0, 7369.9999999999618, 2422.4999999999909, 31354.999999999989, 31562.499999999989, 7997.5000000000109, 16499.999999999993, 11390.000000000031, 16992.499999999993, 12774.999999999989, 6027.4999999999982, 34089.999999999978, 11680.000000000022, 10292.500000000018, 13357.500000000005, 17204.999999999985, 9232.4999999999582, 16090.000000000033, 9667.4999999999836, -805.00000000001637, 28245.000000000015, 22357.500000000058, -8042.5000000000164, 24722.500000000029]
print tmPayoff
plt.hist(tmPayoff)
#plt.plot(tmPayoff)
print sum(tmPayoff)
"""
