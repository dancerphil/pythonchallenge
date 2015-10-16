# -*- coding: utf-8 -*- 
'''
Created on 2015年10月16日11时32分

@author: dancephil
'''

# 1
import urllib
# s='12345'
# s='8022'
# s='82682' # one interesting number, and I haven't meet the problem
s='66831' # final number
while 1 :
    f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+s)
    ls = f.readlines()
    for l in ls :
        print l
        for i in l.split(" "):
            s=i
    if not s.isdigit():
        break
    print s

