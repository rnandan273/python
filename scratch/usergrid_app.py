# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 15:04:48 2014

@author: raghu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 11:42:38 2014

@author: raghu
"""

import pycurl, json


class ResponseReader:
   def __init__(self):
       self.contents = ''

   def body_callback(self, buf):
       self.contents = self.contents + buf
      

t = ResponseReader()

def addAdmin(hostname,orgName,adminName,email,adminPasswd): 
    jsonData={}
    jsonData["name"]="Admin"
    jsonData["password"]=adminPasswd
    jsonData["organization"]=orgName
    jsonData["username"]=adminName
    jsonData["email"]=email
    
    data = json.dumps(jsonData)
    urltoPost = hostname+"management/organizations"
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urltoPost)
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()

def addMarketer(hostname,orgName,marketerName,email,marketerPasswd): 
    jsonData={}
    jsonData["name"]="Marketer"
    jsonData["password"]=marketerPasswd
    jsonData["organization"]=orgName
    jsonData["username"]=marketerName
    jsonData["email"]=email
    
    data = json.dumps(jsonData)
    urltoPost = hostname+"management/organizations"
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urltoPost)
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()


def getAdminToken(hostname,adminName,adminPasswd):
    urlToGet=hostname+"management/token?grant_type=password&username="+adminName+"&password="+adminPasswd

    headers=[]
    headers.append('Accept: application/json') 
 
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urlToGet)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.perform()

def addApplication(hostname,orgName,appName,adminToken):
    jsonData = {}
    jsonData["name"]=appName
    
    
    data = json.dumps(jsonData)
    urltoPost =hostname+"management/orgs/"+orgName+"/apps"
   
    headers=[]
    headers.append('Content-Type: application/json')
    token = 'Authorization: Bearer %s' % adminToken
    headers.append(token.encode('ascii'))
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urltoPost)
    c.setopt(pycurl.HTTPHEADER,headers)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()
    
def addApplicationUser(hostname,orgName,appName,userName,userPwd,userEmail,adminToken,userDesignation):    
    jsonData = {}
    jsonData["username"]=userName
    jsonData["password"]=userPwd
    jsonData["email"]=userEmail
    jsonData["designation"]=userDesignation
    data = json.dumps(jsonData)
    urltoPost =hostname+orgName+"/"+appName+"/users"
    c = pycurl.Curl()
    
    headers=[]
    headers.append('Content-Type: application/json')
    token = 'Authorization: Bearer %s' % adminToken
    headers.append(token.encode('ascii'))
    
    c.setopt(pycurl.URL, urltoPost)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()

def getAppUserToken(hostname,orgName,appName,userName,userPasswd):
    print "Getting App user Token"
    urlToGet=hostname+orgName+"/"+appName+"/token?grant_type=password&username="+userName+"&password="+userPasswd
    headers=[]
    headers.append('Accept: application/json') 
    
    print "urlToGet ->",urlToGet
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urlToGet)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.perform()

def addUserAppData(hostname,orgName,appName,dataNode,userToken):
    jsonData = [ { "cat":"fluffy" }, { "fish": { "gold":2, "oscar":1 } } ]
    data = json.dumps(jsonData)
    urltoPost =hostname+orgName+"/"+appName+"/"+dataNode
    headers=[]
    headers.append('Content-Type: application/json')
    token = 'Authorization: Bearer %s' % userToken
    headers.append(token.encode('ascii'))
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urltoPost)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()
    
def getAppUsers(hostname,orgName,appName,adminToken):
    #urlToGet=hostname+orgName+"/"+appName+"/users?limit=200"
    
    urlToGet=hostname+orgName+"/"+appName+"/users?accessToken="+adminToken.encode('ascii')+"&ql=username='*'"
    #urlToGet=hostname+orgName+"/"+appName+"/users?accessToken="+adminToken.encode('ascii')+"&ql=username='raghu'ANDdesignation='Engineering'"
    print urlToGet
    headers=[]
    headers.append('Content-Type: application/json')
    token = 'Authorization: Bearer %s' % adminToken
    headers.append(token.encode('ascii')) 
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urlToGet)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.perform()
    
def addNetworkApplication(hostname):
    getAdminToken(hostname,"ramesh","password")
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']

    orgName="network"
    appName="mailserver"
    addApplication(hostname,orgName,appName,adminToken)

def addEngineeringApplication(hostname):
    getAdminToken(hostname,"ajay","password")
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']

    orgName="reflektion"
    appName="development"
    addApplication(hostname,orgName,appName,adminToken)
    
def addFinanceApplication(hostname):
    getAdminToken(hostname,"raghu","password")
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']

    orgName="finance"
    appName="payroll"
    addApplication(hostname,orgName,appName,adminToken)

def populateMailUsers(hostname,orgName,appName,adminToken,usr):
    print "populating mail user %s"%usr
    user=usr
    userPwd="password"
    email="@gmail.com"
    userName = "%s"%(user)
    userDesignation="Marketer"
    userEmail = "%s%s"%(userName,email)
    addApplicationUser(hostname,orgName,appName,userName,userPwd,userEmail,adminToken,userDesignation)
    
def populateEngineeringUsers(hostname,orgName,appName,adminToken,usr):
    print "populating mail user %s"%usr
    user=usr
    userPwd="password"
    email="@gmail.com"
    userName = "%s"%(user)
    userDesignation="Engineering"
    userEmail = "%s%s"%(userName,email)
    addApplicationUser(hostname,orgName,appName,userName,userPwd,userEmail,adminToken,userDesignation)
    
def populateFinanceUsers(hostname,orgName,appName,adminToken,usr):
    print "populating mail user %s"%usr
    user=usr
    userPwd="password"
    email="@gmail.com"
    userName = "%s"%(user)
    userDesignation="Engineering"
    userEmail = "%s%s"%(userName,email)
    addApplicationUser(hostname,orgName,appName,userName,userPwd,userEmail,adminToken,userDesignation)
    
def populateUsers(hostname,orgName,appName,adminToken,numUsers):
    print "populating users"
    user="user"
    userPwd="password"
    email="@gmail.com"
    
    for i in range(2,numUsers):
        userName = "%s%i"%(user,i)
        userDesignation="Marketer"
        userEmail = "%s%s"%(userName,email)
        print userName
        addApplicationUser(hostname,orgName,appName,userName,userPwd,userEmail,adminToken,userDesignation)
        print "Done"
    """
        
    for i in range(101,200):
        userName = "%s%i"%(user,i)
        userDesignation="Administrators"
        userEmail = "%s%s"%(userName,email)
        print userName
        addApplicationUser(hostname,orgName,appName,userName,userPwd,userEmail,adminToken,userDesignation)
        print "Done"
    """
    
def addMailUsers(hostname,users):
    adminUserName="ramesh"
    adminPasswd="password"
    getAdminToken(hostname,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    orgName="network"
    appName="mailserver"

    created_users = map(lambda usr: populateMailUsers(hostname,orgName,appName,adminToken,usr),users)

def addEngineeringUsers(hostname,users):
    adminUserName="ajay"
    adminPasswd="password"
    getAdminToken(hostname,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    orgName="reflektion"
    appName="development"

    created_users = map(lambda usr: populateEngineeringUsers(hostname,orgName,appName,adminToken,usr),users)

def addFinanceUsers(hostname,users):
    adminUserName="raghu"
    adminPasswd="password"
    getAdminToken(hostname,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    orgName="finance"
    appName="payroll"

    created_users = map(lambda usr: populateFinanceUsers(hostname,orgName,appName,adminToken,usr),users)
    
def addUsers(hostname):
    adminUserName="sysorgadmin"
    adminPasswd="password"
    getAdminToken(hostname,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    orgName="finance"
    appName="payroll"
    populateUsers(hostname,orgName,appName,adminToken,5)
    
def searchUsers(hostname):
    adminUserName="sysorgadmin"
    adminPasswd="password"
    getAdminToken(hostname,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken   
    orgName="sysorg"
    appName="systemapp"
    getAppUsers(hostname,orgName,appName,adminToken)
    print t.contents

def searchNetworkUsers(hostname):
    adminUserName="ramesh"
    adminPasswd="password"
    getAdminToken(hostname,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    orgName="network"
    appName="mailserver"
    getAppUsers(hostname,orgName,appName,adminToken)
    print t.contents

def searchEngineeringUsers(hostname):
    adminUserName="ajay"
    adminPasswd="password"
    getAdminToken(hostname,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    orgName="reflektion"
    appName="development"
    getAppUsers(hostname,orgName,appName,adminToken)
    print t.contents

def searchFinanceUsers(hostname):
    adminUserName="raghu"
    adminPasswd="password"
    getAdminToken(hostname,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    orgName="finance"
    appName="payroll"
    getAppUsers(hostname,orgName,appName,adminToken)
    print t.contents
    
def addFollowRelationship(hostname,user_1,user_2):
    adminUserName=user_2
    adminPasswd="password"
    orgName="finance"
    appName="payroll"
    jsonData = {}
    jsonData["name"]=appName
    
    
    data = json.dumps(jsonData)
    #getAdminToken(hostname,adminUserName,adminPasswd)
    getAppUserToken(hostname,orgName,appName,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    urltoPost =hostname+orgName+"/"+appName+"/users/"+user_1+"/following/users/"+user_2
    #urltoPost =hostname+orgName+"/"+appName+"/users/"+user_2+"/followers/users/"+user_1
    print urltoPost
    
  
    headers=[]
    #headers.append('Content-Type: application/json')
    token = 'Authorization: Bearer %s' % adminToken
    headers.append(token.encode('ascii'))
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urltoPost)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.VERBOSE, True)
    c.setopt(pycurl.POSTFIELDS,data)
    c.setopt(pycurl.POST, 1)
    c.perform()
    print t.contents
    
def queryFollowers(hostname,user_1):
    adminUserName="vijay"
    adminPasswd="password"
    orgName="finance"
    appName="payroll"
    #getAdminToken(hostname,adminUserName,adminPasswd)
    getAppUserToken(hostname,orgName,appName,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    urlToGet =hostname+orgName+"/"+appName+"/users/"+user_1+"/followers"
    #urlToGet =hostname+orgName+"/"+appName+"/users/"+user_1+"/connections/"
    print urlToGet
    headers=[]
    headers.append('Content-Type: application/json')
    token = 'Authorization: Bearer %s' % adminToken
    headers.append(token.encode('ascii')) 
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urlToGet)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.VERBOSE, True)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.perform()
    print t.contents

def postComments(hostname,user):
    adminUserName=user
    adminPasswd="password"
    orgName="finance"
    appName="payroll"
    jsonData = {}
    jsonData["verb"]="Test comment activity"
    
    
    data = json.dumps(jsonData)
    #getAdminToken(hostname,adminUserName,adminPasswd)
    getAppUserToken(hostname,orgName,appName,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    urltoPost =hostname+orgName+"/"+appName+"/users/"+user+"/activities"
    #urltoPost =hostname+orgName+"/"+appName+"/users/"+user_2+"/followers/users/"+user_1
    print urltoPost
    
  
    headers=[]
    headers.append('Content-Type: application/json')
    token = 'Authorization: Bearer %s' % adminToken
    headers.append(token.encode('ascii'))
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urltoPost)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.VERBOSE, True)
    c.setopt(pycurl.POSTFIELDS,data)
    c.setopt(pycurl.POST, 1)
    c.perform()
    print t.contents

def queryFeeds(hostname,user_1):
    adminUserName=user_1
    adminPasswd="password"
    orgName="finance"
    appName="payroll"
    #getAdminToken(hostname,adminUserName,adminPasswd)
    getAppUserToken(hostname,orgName,appName,adminUserName,adminPasswd)
    print t.contents
    content = json.loads(t.contents)
    adminToken=content['access_token']
    print "adminToken -> ",adminToken
    
    urlToGet =hostname+orgName+"/"+appName+"/users/"+user_1+"/feed"
    #urlToGet =hostname+orgName+"/"+appName+"/users/"+user_1+"/connections/"
    print urlToGet
    headers=[]
    headers.append('Content-Type: application/json')
    token = 'Authorization: Bearer %s' % adminToken
    headers.append(token.encode('ascii')) 
    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, urlToGet)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.VERBOSE, True)
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.perform()
    print t.contents
    
def showUserDetails():
    orgName="sysorg"
    appName="systemapp"
    userName="raghu.sk@gmail.com"
    userPwd="Raghu1994"
    userEmail="raghu.sk@gmail.com"
    
    """
    userDesignation="Marketer"
    
    userName="user0"
    userPwd="password"
    userEmail="user0@gmail.com"
    userDesignation="Marketer"
    """
    #addApplicationUser(hostname,orgName,appName,userName,userPwd,userEmail,adminToken,userDesignation)
    #print t.contents
    # get App user token
    getAppUserToken(hostname,orgName,appName,userName,userPwd)
    print "content 1 ->",t.contents
    content = json.loads(t.contents)
    print "content 2 ->",content
    userToken=content['access_token']
    print "userToken -> ",userToken

    """
    # Add user data
    dataNode="projName"
    addUserAppData(hostname,orgName,appName,dataNode,userToken)
    print t.contents
    """
    
hostname = "http://localhost:8080/"  

#Department registration
#addAdmin(hostname,"network","ramesh","ramesh@ltp.com","password")
#addAdmin(hostname,"finance","raghu","raghu@ltp.com","password")
#addAdmin(hostname,"reflektion","ajay","ajay@ltp.com","password")

# Application registration
#addNetworkApplication(hostname)
#addEngineeringApplication(hostname)
#addFinanceApplication(hostname)

#Application user registration
users=['raghu','ajay','vijay','venki']
#addEngineeringUsers(hostname,users)

users=['raghu','ajay','vijay','venki','ramesh','amit','gopal']
#addFinanceUsers(hostname,users)

users=['raghu','ajay','amit','venki','vijay']
#addMailUsers(hostname,users)

#Queries
#searchNetworkUsers(hostname)
searchEngineeringUsers(hostname)
#searchFinanceUsers(hostname)

#Model followers
#addFollowRelationship(hostname,"venki","vijay")
#addFollowRelationship(hostname,"amit","vijay")
#addFollowRelationship(hostname,"raghu","vijay")
#addFollowRelationship(hostname,"gopal","vijay")
#addFollowRelationship(hostname,'raghu_1','vijay')
#queryFollowers(hostname,"vijay")

#post comments
#postComments(hostname,"vijay")

#query feeds by all followers
#queryFeeds(hostname,"vijay")
#queryFeeds(hostname,"raghu_1")
#queryFeeds(hostname,"ajay")
#queryFeeds(hostname,"gopal")



        
