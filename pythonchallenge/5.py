# -*- coding: utf-8 -*- 
'''
Created on 2015年10月16日12时48分

@author: dancerphil
'''

# 1
import pickle
import urllib
f= urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
banner= pickle.load(f)
for line in banner:
    print(''.join(map(lambda x: x[0]* x[1], line)))

# # 2
# import pickle
# import urllib
# f= urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
# banner= pickle.load(f)
# news=''
# for line in banner:
#     for term in line:
#         for i in range(term[1]):
#             news+=term[0]
#     news+='\n'
# print news
