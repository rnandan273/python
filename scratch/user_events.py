# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 14:47:50 2014

@author: raghu
"""

import json
import time
import datetime
import pycurl

userDict={}

def getGlobalTime():
    start_date = "2012-09-28 20:30:55.78200"
    global_time = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S.%f")
    gt = (global_time-datetime.datetime.utcfromtimestamp(0)).total_seconds()
    return gt
    
def getUserGlobalSlot(t1,uid):
    
    gts = (userDict[uid]+(30*60*t1)-getGlobalTime())/(30*60)
    print "gts",gts
    return gts
    
def getUserSlot(t1,uid):
    if(userDict.has_key(uid)):
        return (t1 - userDict[uid])/(30*60)
    else:
        userDict[uid]=t1
        return 0

    
def readJson(filename):
    start_time = time.time()
    print start_time
        
    print "START----------->",datetime.datetime.utcfromtimestamp(start_time/1000).strftime('%Y-%m-%d %H:%M:%S')
    view_event_file=open(filename)
    cnt=0
 
    for line in view_event_file:
        if(cnt>-1):
            view_event = json.loads(line)
            keys= view_event.keys()
            """
            x = map(lambda key: processEventKeys(key,view_event), keys)
            xx=filter(lambda key:key!=False,x)
            """
            pInfo = map(lambda key: processEventKeys(key,view_event), keys)                       
            pInfo = filter(lambda key:key!=False,pInfo)
        
            if(size(pInfo) == 3):
                modInfo = map(lambda key: splitEventDetails(key,pInfo), pInfo[0])  
            """
            else:
                print "Ignoring this event"
            """
            
            map(lambda key: publishToES(key), modInfo)
        cnt=cnt+1
    end_time = time.time()

    print "Total time in seconds->",((end_time-start_time))

class ResponseReader:
   def __init__(self):
       self.contents = ''

   def body_callback(self, buf):
       self.contents = self.contents + buf
      
t = ResponseReader()

def publishToES(event):   

    hostname = "http://localhost:9200/test/userevents/"
    
    data = json.dumps(event)
    #print "Publishing to ES",hostname
    
    urltoPost = hostname
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urltoPost)
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()
    
    
    #print t.contents


    
    
def splitEventDetails(key,validPinfo):
    pubInfo={}
    pubInfo['product']=validPinfo[1]
    pubInfo['userid']=validPinfo[2]
    key['ts']=getUserSlot(key['ts'],validPinfo[2]['uid'])
    key['gts']=getUserGlobalSlot(key['ts'],validPinfo[2]['uid'])
    pubInfo['event']=key
    return pubInfo
    
def processEventKeys(key,view_event):
        #print "processing ",key,view_event[key]
        """
    t = (  (key=='ordered_events' and filter(filterEventDetails,map(orderedEventDetails,view_event[key])) \
        or (key=='attributes' and filter(filterEventAttributes,map(attributeDetails,view_event[key]))) \
        or (key=='products' and filter(filterProductDetails,map(productDetails,view_event[key])))
        or printOthers(key,view_event[key])))
        """
        t = ( (key=='ordered_events' and filter(filterEventDetails,map(orderedEventDetails,view_event[key])) \
        or (key=='products' and filter(filterProductDetails,map(productDetails,view_event[key]))) \
        or (key=='id' and printOthers(key,view_event[key]))))
        """
        t = ( (key=='ordered_events' and filter(filterEventDetails,map(orderedEventDetails,view_event[key])) \
        or (key=='products' and filter(filterProductDetails,map(productDetails,view_event[key]))))) 
        
        """
        return t
    
def filterEventAttributes(value):
    #print "Filtering Attributes->",value
    return 1
    

def filterEventDetails(value):
    evtDetails = eval(value['eventDetail'])
    validEventValues=filter(lambda key:evtDetails[key]==1,evtDetails.keys())
    if size(validEventValues) == 0 : 
        return 0 
    else: 
        return 1
        
    
def filterProductDetails(value):  
    #print "Filtering Product Details->",value
    return 1
    
def printOthers(key,value):
    #print ""
    """
    print "Key -------> ",key
    print "Value -----> ",value
    """
    user_attr={}
    user_attr['uid']=value
    return user_attr

def productDetails(pr):
    #print "PRODUCT ->",pr
    product_details={}
    product_details['pid']=pr['pid']
    return product_details

def orderedEventDetails(oev):
    eventDetail={}
    eventDetail['ts'] = oev['ts']
    eventDetail['eventDetail']=oev['eventDetails']
    eventDetail['eventUri']=oev['eventUri']
    return eventDetail

def attributeDetails(attr):
    #print attr , attr.keys()
    user_attr={}
    user_attr['uid']=attr['attr_value']
    return user_attr

def searchDataQuery(qDate1,qDate2):
    """
    ts = datetime.datetime.strptime(qDate1, "%Y-%m-%d %H:%M:%S.%f")
    t1 = (ts - datetime.datetime.utcfromtimestamp(0)).total_seconds()

    gs1 = getUserGlobalSlot(t1) 
    
    ts = datetime.datetime.strptime(qDate2, "%Y-%m-%d %H:%M:%S.%f")
    t2 = (ts - datetime.datetime.utcfromtimestamp(0)).total_seconds()
    
    gs2 = getUserGlobalSlot(t2)
    
    print gs1, gs2
    # range queries between these global slots
    
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
    """    

dt1 = "2014-04-28 20:30:55.78200"
dt2 = "2014-05-28 20:30:55.78200"
    
searchDataQuery(dt1,dt2)


#filename="/Users/raghu/work/projects/refk/a1.json"
filename="/Users/raghu/work/projects/refk/user_history.json"
readJson(filename)