# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 23:00:08 2014

@author: raghu
"""

import pycurl
import time
import datetime

from datetime import timedelta


def f(x): 
    return x % 2 != 0 and x % 3 != 0

def cube(x): 
    return x*x*x
    
fx = filter(f, range(2, 25))
print fx

vx = map(cube, filter(f, range(2, 25)))

print vx

def add(x,y): 
    return x+y
    
print "Reduce ",reduce(add, vx)

class ResponseReader:
   def __init__(self):
       self.contents = ''

   def body_callback(self, buf):
       self.contents = self.contents + buf
  

t = ResponseReader()

def searchData():
    urlToGet="http://localhost:9200/test/userevents/_search?eventUri=page_view_http://www.oneillclothing.com"
    urlToGet="http://localhost:9200/test/userevents/_search?pid=254973"
    urlToGet="http://localhost:9200/test/userevents/_count?"
    print urlToGet
    headers=[]
    headers.append('Content-Type: application/json')
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urlToGet)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.perform()
    
    print t.contents
    string_date = "2013-09-28 20:30:55.78200"
    t3 = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S.%f")
    print t3
    t3=t3+timedelta(days=-10)
    print t3
    t2 = (t3 - datetime.datetime.utcfromtimestamp(0)).total_seconds()
    start_time = time.time()
    print "Start time -> ",start_time,t2
    
    current = datetime.datetime.now()
    print current
    #current =current+ timedelta(days=-10)
    current =current+ timedelta(seconds=-10)
    print current

def searchDataQuery(qDate1,qDate2):
    urlToGet="http://localhost:9200/test/userevents/_search?eventUri=page_view_http://www.oneillclothing.com"
    urlToGet="http://localhost:9200/test/userevents/_search?pid=254973"
    urlToGet="http://localhost:9200/test/userevents/_count?"
    print urlToGet
    headers=[]
    headers.append('Content-Type: application/json')
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urlToGet)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.perform()
    
    print t.contents

    ts = datetime.datetime.strptime(qDate1, "%Y-%m-%d %H:%M:%S.%f")
    t1 = (ts - datetime.datetime.utcfromtimestamp(0)).total_seconds()

    gs1 = getUserGlobalSlot(t1)
    
    ts = datetime.datetime.strptime(qDate2, "%Y-%m-%d %H:%M:%S.%f")
    t2 = (ts - datetime.datetime.utcfromtimestamp(0)).total_seconds()
    
    gs2 = getUserGlobalSlot(t1)
    
    start_time = time.time()
    print "Start time -> ",start_time,t2
    
    current = datetime.datetime.now()
    print current
    #current =current+ timedelta(days=-10)
    current =current+ timedelta(seconds=-10)
    print current

#searchData()
#searchDataQuery(t1)
cp=[521,421,321,221,121,90,60,30,20,10]
pp=[11,21,31,6191,121,221,321,421,521]
c_qty=[0,0,0,0,1,-1,-2,1,0,0]
p_qty=[0,0,0,0,1,0,0,0,0,0]
def f1(x): 
    return x*100+6000    
strikePrices = map(f1, range(1, 10))
print "strikePrices",strikePrices


cOrder=zip(c_qty,cp,strikePrices)
pOrder=zip(p_qty,pp,strikePrices)

def add(x,y):
    return x+y
    
def callPayOff(sp,cOrder):
    payoff = map(lambda x:getOrderForStrikePricePayoff(x,sp),cOrder)
    netPayoff=reduce(add,payoff)
    return netPayoff
  
def getOrderForStrikePricePayoff(x,sp):
    if sp>=x[2]:
        payoff = x[0]*(sp-x[2]-x[1])
        return payoff
    else:
        return -x[1]*x[0]
      
netPayoff = map(lambda x:callPayOff(x,cOrder),strikePrices)
print netPayoff



    
