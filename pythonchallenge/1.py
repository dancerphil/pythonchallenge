# -*- coding: utf-8 -*- 
import string
'''
Created on 2015年10月16日

@author: hp
'''

# # 1
# s=r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# news=""
# for i in s:
#     t=ord(i)
#     if ( i >= 'a' and i <= 'z' ):
#         t+=2
#     if i =='y' or i== 'z':
#         t-=26
#     news+=chr(t)
# print news

# 2
s=r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = string.maketrans(intab, outtab)
print string.translate(s,trantab)

s2=r"http://www.pythonchallenge.com/pc/def/map.html"
print string.translate(s2,trantab)
