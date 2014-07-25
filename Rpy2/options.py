# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 23:50:57 2014

@author: raghu
"""

#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def buyCallOption(strikePrice,premium,start,numElements):   
    xaxis = getXAxis(start,numElements)
    cost = -premium*np.ones(numElements)
    coeff = getXAxis(start,numElements)
    coeff[coeff>strikePrice]=strikePrice
    net = cost+(xaxis -coeff)
    return net

def sellCallOption(strikePrice,premium,start,numElements):    
    xaxis = getXAxis(start,numElements)
    cost = premium*np.ones(numElements)
    coeff = getXAxis(start,numElements)
    coeff[coeff>strikePrice]=strikePrice
    net = cost+(-xaxis +coeff)
    return net

def buyPutOption(strikePrice,premium,start,numElements):    
    xaxis = getXAxis(start,numElements)
    cost = -premium*np.ones(numElements)
    coeff = getXAxis(start,numElements)
    coeff[coeff<strikePrice]=strikePrice
    net = cost+(-xaxis +coeff)
    return net
    
def sellPutOption(strikePrice,premium,start,numElements):    
    xaxis = getXAxis(start,numElements)
    cost = premium*np.ones(numElements)
    coeff = getXAxis(start,numElements)
    coeff[coeff<strikePrice]=strikePrice
    net = cost+(xaxis -coeff)
    return net

def getXAxis(origin,numElements):
    arr = np.arange(numElements)
    return origin+100*arr
    
def buyNiftyCallOption(strikePrice,premium):
    print "Buy NiftyCall %d @%d"%(strikePrice,premium)
    return 50*buyCallOption(strikePrice,premium,6000,20)

def sellNiftyCallOption(strikePrice,premium):
    print "Sell NiftyCall %d @%d"%(strikePrice,premium)
    return 50*sellCallOption(strikePrice,premium,6000,20)
    
def buyNiftyPutOption(strikePrice,premium):
    print "Buy NiftyPut %d @%d"%(strikePrice,premium)
    return 50*buyPutOption(strikePrice,premium,6000,20)

def sellNiftyPutOption(strikePrice,premium):
    print "Sell NiftyPut %d @%d"%(strikePrice,premium)
    return 50*sellPutOption(strikePrice,premium,6000,20)

def buyNiftyFuture(strikePrice,premium):
    print "Buy NiftyFuture %d @%d"%(strikePrice,premium)
    return sellNiftyPutOption(strikePrice,0)+buyNiftyCallOption(strikePrice,premium)
    
def sellNiftyFuture(strikePrice,premium):
    print "Sell NiftyCall %d @%d"%(strikePrice,premium)
    return buyNiftyPutOption(strikePrice,premium)+sellNiftyCallOption(strikePrice,0)
    
def buyBankNiftyCallOption(strikePrice,premium):
    return buyCallOption(strikePrice,premium,10000,50)
    
def buyBankNiftyPutOption(strikePrice,premium):
    return buyPutOption(strikePrice,premium,10000,50)
    
def longNiftyStraddle(strikePrice,cp,pp):
    netpayoff = buyNiftyCallOption(strikePrice,cp)+buyNiftyPutOption(strikePrice,pp)
    return netpayoff
     
def shortNiftyStraddle(strikePrice,cp,pp):
    netpayoff = sellNiftyCallOption(strikePrice,cp)+sellNiftyPutOption(strikePrice,pp)
    return netpayoff

def longNiftyStrangle(sp1,sp2,cp,pp):
    netpayoff = buyNiftyCallOption(sp1,cp)+buyNiftyPutOption(sp2,pp)
    return netpayoff
     
def shortNiftyStrangle(sp1,sp2,cp,pp):
    netpayoff = sellNiftyCallOption(sp1,cp)+sellNiftyPutOption(sp2,pp)
    return netpayoff
     
def longNiftyCallButterfly(sp1,cp1,sp2,cp2,sp3,cp3):
    netpayoff = buyNiftyCallOption(sp1,cp1)+2*sellNiftyCallOption(sp2,cp2)+buyNiftyCallOption(sp3,cp3)
    return netpayoff

def shortNiftyCallButterfly(sp1,cp1,sp2,cp2,sp3,cp3):
    netpayoff = sellNiftyCallOption(sp1,cp1)+2*buyNiftyCallOption(sp2,cp2)+sellNiftyCallOption(sp3,cp3)
    return netpayoff

def longNiftyPutButterfly(sp1,pp1,sp2,pp2,sp3,pp3):
    netpayoff = buyNiftyPutOption(sp1,pp1)+2*sellNiftyPutOption(sp2,pp2)+buyNiftyPutOption(sp3,pp3)
    return netpayoff

def shortNiftyPutButterfly(sp1,pp1,sp2,pp2,sp3,pp3):
    netpayoff = sellNiftyPutOption(sp1,pp1)+2*buyNiftyPutOption(sp2,pp2)+sellNiftyPutOption(sp3,pp3)
    return netpayoff

def longNiftyCallSpread(sp1,cp1,sp2,cp2):
    netpayoff = buyNiftyCallOption(sp1,cp1)+(sellNiftyCallOption(sp2,cp2))
    return netpayoff

def longNiftyPutSpread(sp1,pp1,sp2,pp2):
    netpayoff = buyNiftyPutOption(sp1,pp1)+sellNiftyPutOption(sp2,pp2)
    return netpayoff

def shortNiftyCallSpread(sp1,cp1,sp2,cp2):
    netpayoff = sellNiftyCallOption(sp1,cp1)+buyNiftyCallOption(sp2,cp2)
    return netpayoff

def shortNiftyPutSpread(sp1,pp1,sp2,pp2):
    netpayoff = sellNiftyPutOption(sp1,pp1)+buyNiftyPutOption(sp2,pp2)
    return netpayoff

def longIronCondor(sp1,pp1,sp2,pp2,sp3,cp3,sp4,cp4):
    netpayoff =shortNiftyPutSpread(sp1,pp1,sp2,pp2) +shortNiftyCallSpread(sp3,cp3,sp4,cp4)  
    return netpayoff

def shortIronCondor(sp1,pp1,sp2,pp2,sp3,cp3,sp4,cp4):
    netpayoff =longNiftyPutSpread(sp1,pp1,sp2,pp2) +longNiftyCallSpread(sp3,cp3,sp4,cp4)  
    return netpayoff

def longIronButterfly(sp1,pp1,sp2,pp2,sp3,cp3,sp4,cp4):
    netpayoff =longIronCondor(sp1,pp1,sp2,pp2,sp3,cp3,sp4,cp4)  
    return netpayoff

def shortIronButterfly(sp1,pp1,sp2,pp2,sp3,cp3,sp4,cp4):
    netpayoff =shortIronCondor(sp1,pp1,sp2,pp2,sp3,cp3,sp4,cp4)  
    return netpayoff
    
def longCondorWithCalls(sp1,cp1,sp2,cp2,sp3,cp3,sp4,cp4):
    netpayoff =longNiftyCallSpread(sp1,cp1,sp2,cp2) +shortNiftyCallSpread(sp3,cp3,sp4,cp4)  
    return netpayoff

def shortCondorWithCalls(sp1,cp1,sp2,cp2,sp3,cp3,sp4,cp4):
    netpayoff =shortNiftyCallSpread(sp1,cp1,sp2,cp2) +longNiftyCallSpread(sp3,cp3,sp4,cp4)  
    return netpayoff

def shortCondorWithPuts(sp1,pp1,sp2,pp2,sp3,pp3,sp4,pp4):
    netpayoff =shortNiftyPutSpread(sp1,pp1,sp2,pp2) +longNiftyPutSpread(sp3,pp3,sp4,pp4)  
    return netpayoff

def longCondorWithPuts(sp1,pp1,sp2,pp2,sp3,pp3,sp4,pp4):
    netpayoff =longNiftyPutSpread(sp1,pp1,sp2,pp2) +shortNiftyPutSpread(sp3,pp3,sp4,pp4)  
    return netpayoff

def DeepInTheMoneyCoveredCallStrategy(sp1,cp1,sp2,cp2):
    return longNiftyCallSpread(sp1,cp1,sp2,cp2)

def SkipStrikeButterflyWithCalls(sp1,cp1,sp2,cp2,sp3,cp3):
    return longNiftyCallButterfly(sp1,cp1,sp2,cp2,sp3,cp3) + shortNiftyCallSpread(sp2,cp2,sp3,cp3)

def SkipStrikeButterflyWithPuts(sp1,pp1,sp2,pp2,sp3,pp3):
    return longNiftyPutButterfly(sp1,pp1,sp2,pp2,sp3,pp3) + shortNiftyPutSpread(sp2,pp2,sp3,pp3)

def SlingShot(sp1,cp1,sp2,cp2,sp3,cp3,sp4,cp4):
    netpayoff = longNiftyCallButterfly(sp1,cp1,sp2,cp2,sp3,cp3)+buyNiftyCallOption(sp4,cp4)
    return netpayoff

def longNiftyCollar(sp1,cp1,sp2,cp2,sp3,pp3):
    netpayoff = buyNiftyFuture(sp1,cp1) + sellNiftyCallOption(sp2,cp2)+buyNiftyPutOption(sp3,pp3)
    return netpayoff

def ChristmasTreeWithCalls(sp1,cp1,sp3,cp3,sp4,cp4):
    return buyNiftyCallOption(sp1,cp1)+3*sellNiftyCallOption(sp3,cp3)+buyNiftyCallOption(sp4,cp4)

def callLadder(sp1,cp1,sp2,cp2):
    return sellNiftyCallOption(sp1,cp1)+2*buyNiftyCallOption(sp2,cp2)

def putLadder(sp1,cp1,sp2,cp2):
    return sellNiftyPutOption(sp1,cp1)+2*buyNiftyPutOption(sp2,cp2)

def testBankNifty():
    netpayoff = 25*buyBankNiftyCallOption(13000,653)
    netpayoff = netpayoff+25*buyBankNiftyPutOption(13000,583)
    plt.plot(getXAxis(10000,50), 5*netpayoff)
    print netpayoff

def getStrikes():
    strikePrice =[6000,6100,6200,6300,6400,6500,6600,6700,6800,6900,7000,7100,7200,7300,7400]
    return strikePrice
    
def getCallPremiun():
    callPremium =[759,649,585,506,437,368,307,251,201,161,123,92,67,48,35]
    return callPremium

def getPutPremium():
    putPremium =[28,38,54,74,99,131,168,210,258,315,377,446,518,594,677]
    return putPremium
    
def getCSP(index):
    strikePrice=getStrikes()
    csp=[]    
    csp0 = strikePrice[index]
    csp.append(csp0)
    csp1 = strikePrice[index+1]
    csp.append(csp1)
    csp2 = strikePrice[index+2]
    csp.append(csp2)
    csp3 = strikePrice[index+3]
    csp.append(csp3)
    csp4 = strikePrice[index+4]
    csp.append(csp4)
    csp5 = strikePrice[index+5]
    csp.append(csp5)
    csp6 = strikePrice[index+6]
    csp.append(csp6)
    return csp
    
def getPSP(index):
    strikePrice=getStrikes()
    psp=[]
    psp0 = strikePrice[index] 
    psp.append(psp0)
    psp1 = strikePrice[index-1]
    psp.append(psp1)
    psp2 = strikePrice[index-2]
    psp.append(psp2)
    psp3 = strikePrice[index-3]
    psp.append(psp3)
    psp4 = strikePrice[index-4]
    psp.append(psp4)
    psp5 = strikePrice[index-5]
    psp.append(psp5)
    psp6 = strikePrice[index-6]
    psp.append(psp6)
    return psp
    
def getCP(index):
    strikePrice=getStrikes()
    callPremium=getCallPremiun()
    csp=[]
    cp0 = callPremium[index]
    csp.append(cp0)
    cp1 = callPremium[index+1]
    csp.append(cp1)
    cp2 = callPremium[index+2]
    csp.append(cp2)
    cp3 = callPremium[index+3]
    csp.append(cp3)
    cp4 = callPremium[index+4]
    csp.append(cp4)
    cp5 = callPremium[index+5]
    csp.append(cp5)
    cp6 = callPremium[index+6]
    csp.append(cp6)
    csp_2 = strikePrice[index-2]
    cp_2 = callPremium[index-2]
    return csp
    
def getPP(index):
    putPremium = getPutPremium()
    psp=[]
    pp0 = putPremium[index]
    psp.append(pp0)
    pp1 = putPremium[index-1]
    psp.append(pp1)
    pp2 = putPremium[index-2]
    psp.append(pp2)
    pp3 = putPremium[index-3]
    psp.append(pp3)
    pp4 = putPremium[index-4]
    psp.append(pp4)
    pp5 = putPremium[index-5]
    psp.append(pp5)
    pp6 = putPremium[index-6]
    psp.append(pp6)
    return psp
    
def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    #including valid will REQUIRE there to be enough datapoints.
    #for example, if you take out valid, it will start @ point one,
    #not having any prior points, so itll be 1+0+0 = 1 /3 = .3333
    smas = np.convolve(values, weigths, 'valid')
    return smas # as a numpy array
    
def analyseTrade():
    axis = getXAxis(6000,20)
    csp= getCSP(7)
    psp= getPSP(7)
    cp=getCP(7)
    pp=getCP(7)

    #payoff=shortNiftyStraddle(csp[0],cp[0],pp[0])
    #payoff = longCondorWithCalls(csp[0],cp[0],csp[2],cp[2],csp[4],cp[4],csp[5],cp[5])
    #csp=getCSP(8)
    #payoff=payoff+sellNiftyCallOption(csp[1],cp[1])
    #csp=getCSP(6)
    #payoff=payoff+sellNiftyCallOption(csp[1],cp[1])
    #payoff=payoff+longNiftyStraddle(csp[0],cp[0],pp[0])
    #payoff = payoff+longCondorWithCalls(csp[0],cp[0],csp[2],cp[2],csp[4],cp[4],csp[5],cp[5])
    #plt.plot(axis,payoff)
    return axis,csp,psp,cp,pp

def testNiftyCollar():
    axis = getXAxis(6000,20)
    csp= getCSP(7)
    psp= getPSP(7)
    cp=getCP(7)
    pp=getCP(7)
    payoff =buyNiftyFuture(6700,60)+sellNiftyCallOption(csp[1],cp[1])
    payoff=payoff+putLadder(psp[0],pp[0],psp[1],pp[1])
    #netpayoff =netpayoff+50*buyNiftyFuture(6800,60)+50*sellNiftyCallOption(6900,210)++50*sellNiftyPutOption(6800,183)
    #netpayoff =netpayoff+50*buyNiftyFuture(6600,60)+150*sellNiftyCallOption(6700,210)
    #netpayoff = netpayoff+50*buyNiftyPutOption(6300,97)
    plt.plot(getXAxis(6000,20), payoff)

    print payoff
    
    
axis,csp,psp,cp,pp=analyseTrade()
plt.plot(axis,longNiftyStraddle(csp[0],cp[0],pp[0]))

#testNiftyCollar()
"""
    #strikePrice =[6000,6100,6200,6300,6400,6500,6600,6700,6800,6900,7000,7100,7200,7300,7400]
    #callPremium =[759,649,585,506,437,368,307,251,201,161,123,92,67,48,35]
    #putPremium =[28,38,54,74,99,131,168,210,258,315,377,446,518,594,677]
payoff = ChristmasTreeWithCalls(csp1,cp1,csp3,cp3,csp4,cp4)
#payoff = longNiftyCallButterfly(csp0,cp0,csp3,cp3,csp5,cp5)+longNiftyCallButterfly(csp2,cp2,csp4,cp4,csp6,cp6)
#payoff = payoff+longNiftyPutButterfly(psp0,pp0,psp3,pp3,psp5,pp5)+longNiftyPutButterfly(psp2,pp2,psp4,pp4,psp6,pp6)
#payoff=shortNiftyStrangle(csp1,psp1,cp1,pp1)+longCondorWithCalls(csp2,cp2,csp4,cp4,csp5,cp5,csp6,cp6)
#payoff = longCondorWithCalls(csp2,cp2,csp3,cp3,csp5,cp5,csp6,cp6)
#payoff = callLadder(csp0,cp0,csp1,cp1)+putLadder(psp0,pp0,psp1,pp1)
#payoff = shortNiftyCallSpread(csp0,cp0,csp1,cp1)+shortNiftyCallSpread(csp2,cp2,csp3,cp3)
#payoff=shortNiftyStrangle(csp1,psp1,cp1,pp1)#+shortNiftyStrangle(csp2,psp2,cp2,pp2)+shortNiftyStrangle(csp3,psp3,cp3,pp3)
#plt.plot(axis,payoff)
////
Library of Strategies
plt.plot(axis,longNiftyStraddle(csp0,cp0,pp0))
plt.plot(axis,shortNiftyStraddle(csp0,cp0,pp0))
plt.plot(axis,longNiftyStrangle(csp1,psp1,cp1,pp1))
plt.plot(axis,shortNiftyStrangle(csp1,psp1,cp1,pp1))
plt.plot(axis,longNiftyCallButterfly(csp0,cp0,csp1,cp1,csp2,cp2))
plt.plot(axis,shortNiftyCallButterfly(csp0,cp0,csp1,cp1,csp2,cp2))
plt.plot(axis,longNiftyPutButterfly(psp0,pp0,psp1,pp1,psp2,pp2))
plt.plot(axis,shortNiftyPutButterfly(psp0,pp0,psp1,pp1,psp2,pp2))
plt.plot(axis,longNiftyCallSpread(csp0,cp0,csp1,cp1))
plt.plot(axis,shortNiftyCallSpread(csp0,cp0,csp1,cp1))
plt.plot(axis,longNiftyPutSpread(psp0,pp0,psp1,pp1))
plt.plot(axis,shortNiftyPutSpread(psp0,pp0,psp1,pp1))
plt.plot(axis,longIronCondor(psp1,pp1,psp2,pp2,csp1,cp1,csp2,cp2))
plt.plot(axis,shortIronCondor(psp1,pp1,psp2,pp2,csp1,cp1,csp2,cp2))
plt.plot(axis,longIronButterfly(psp1,pp1,psp2,pp2,csp1,cp1,csp2,cp2))
plt.plot(axis,shortIronButterfly(psp1,pp1,psp2,pp2,csp1,cp1,csp2,cp2))
plt.plot(axis,longCondorWithCalls(csp1,cp1,csp2,cp2,csp3,cp3,csp4,cp4))
plt.plot(axis,shortCondorWithCalls(csp1,cp1,csp2,cp2,csp3,cp3,csp4,cp4))
plt.plot(axis,shortCondorWithPuts(psp1,pp1,psp2,pp2,psp3,pp3,psp4,pp4))
plt.plot(axis,longCondorWithPuts(psp1,pp1,psp2,pp2,psp3,pp3,psp4,pp4))
plt.plot(axis,DeepInTheMoneyCoveredCallStrategy(csp_2,cp_2,csp0,cp0))
plt.plot(axis,SkipStrikeButterflyWithCalls(csp1,cp1,csp2,cp2,csp4,cp4))
plt.plot(axis,SkipStrikeButterflyWithPuts(psp1,pp1,psp2,pp2,psp4,pp4))
plt.plot(axis,SlingShot(csp1,cp1,csp2,cp2,csp3,cp3,csp4,cp4))
plt.plot(axis,ChristmasTreeWithCalls(csp1,cp1,csp3,cp3,csp4,cp4))
"""


