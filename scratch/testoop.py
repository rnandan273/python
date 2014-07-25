# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 14:54:55 2014

@author: raghu
"""

def f1():
    print "f1"
    return "f1"

def f2():
    print "f2"
    return "f2"

def f3():
    print "f4"
    return "f4"
    
f1_list=[]
f1_list.append(f1)
f1_list.append(f2)

f2_list=[]
f2_list.append(f2)
f2_list.append(f3)


def executor(f,str):
    return f()
    
ex = map(lambda x:executor(x,"1"),f1_list)
print ex

ex = map(lambda x:executor(x,"2"),f2_list)
print ex