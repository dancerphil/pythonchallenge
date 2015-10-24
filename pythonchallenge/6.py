# -*- coding: utf-8 -*- 
'''
Created on 2015年10月16日20时46分

@author: dancerphil
'''
# ss1=["cmd","business","item_name","no_note","currency_code","tax","bn"]
# ss2=["_xclick","thesamet@gmail.com","Python Challenge donations","1","USD","0","PP-DonationsBF"]
# print zip(*zip(ss1,ss2))

# 1
# init
import zipfile
files = zipfile.ZipFile('channel.zip','r')

# step 1
print files.open('readme.txt').read().decode()

# # step 2
# import re
# target = re.compile('Next nothing is (\d*)')# or to use next line
# # target = re.compile('Next nothing is ([0-9]{1,5})')
# suffix = 90052 # hint in readme
# while True:
#     f = str(suffix) + '.txt'
#     txt = files.open(f).read().decode()
#     print txt
#     if target.match(txt):
#         print target.match(txt).groups(0)[0]
#         suffix = target.match(txt).groups(0)[0]
#     else:
#         break

# step 3 
# 1
import re
target = re.compile('Next nothing is (\d*)')
suffix = 90052 # hint in readme
while True:
    f = str(suffix) + '.txt'
    txt = files.open(f).read().decode()
    comment = files.getinfo(f).comment.decode()
    print comment,
    if target.match(txt):
        suffix = target.match(txt).groups(0)[0]
    else:
        break

# # 2
# import re
# target = re.compile('Next nothing is (\d*)')
# suffix = 90052 # hint in readme
# news=''
# while True:
#     f = str(suffix) + '.txt'
#     txt = files.open(f).read().decode()
#     comment = files.getinfo(f).comment.decode()
#     news += comment
#     if target.match(txt):
#         suffix = target.match(txt).groups(0)[0]
#     else:
#         break
# print news

# # useless interesting feature
# for i in files.infolist():
#     print i.comment,

# step 4
import urllib
f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/hockey.html')
ls = f.readlines()
for l in ls :
    print l
# notice that the letter is OXYGEN