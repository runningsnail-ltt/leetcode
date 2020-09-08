# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter

s = set()
y = {"x","y","z"}
s.update(y)
#print s

a = ['A', 'B', 'A', 'B']
#print list(set(a))


x = {6,7,8}
y = {7,8,9}
x1 = x | y
x2 = x & y
x3 = x1-x2
#print x3


def double_list(lst):
    for index,value in enumerate(lst):
        if isinstance(value,bool):
            continue
        if isinstance(value,(int,float)):
            lst[index] = lst[index]*2
        if isinstance(value,list):
            double_list(lst[index])
    return lst
#print double_list([1, [4, 6], True])

dic = {
    'python': 95,
    'java': 99,
    'c': 100
    }
print  len(dic)
dic['java'] = 98
print dic

print (dic.pop('c'),dic)
dic['php'] = 90
print dic
a = list(dic.keys())

b = list(dic.values())
print a,b

print sum(b)
print max(b)
dic1 = {'php': 97}
dic.update(dic1)
print dic


print sum([x for x in range(1,101)])
print [x for x in range(1,101)]
print [pow(x,3) for x in [2,3,4,5] ]

print [(x,y) for x,y in zip(['x','y','z'], [1,2,3])]
