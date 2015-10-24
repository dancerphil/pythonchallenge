# -*- coding: utf-8 -*- 
'''
Created on 2015年10月25日03时44分

@author: dancerphil
'''

# 1
def next(a):
    s=''
    while a!='':
        t=a[0]
        c=0
        while c < len(a) and a[c]==t:
            c+=1
        s+=str(c)+t
        a=a[c:]
    return s

txt=[]
txt.append('1')
for i in range(1,31):
    txt.append(next(txt[i-1]))
#     print i,txt[i]
print len(txt[30])