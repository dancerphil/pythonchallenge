# -*- coding: utf-8 -*- 
'''
Created on 2015年10月16日

@author: dancerphil
'''

# init
s=r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# step 1
# 1
newstring=""
for char in s:
    if char >= 'a' and char <= 'x':
        newstring+=chr(ord(char)+2)
    elif char =='y' or char== 'z':
        newstring+=chr(ord(char)-24)
    else :
        newstring+=char
print newstring

# 2
import string
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = string.maketrans(intab, outtab)
print string.translate(s,trantab)

# step 2
# s2=r"http://www.pythonchallenge.com/pc/def/map.html"
# print string.translate(s2,trantab)
print string.translate("map",trantab)
