# -*- coding: utf-8 -*- 
'''
Created on 2015年10月25日02时59分

@author: dancerphil
'''

# 1
import bz2
un='BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw='BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print bz2.decompress(un)
print bz2.decompress(pw)

# # interesting
# print bz2.decompress(bz2.compress('what the fuck')+bz2.compress('what the fuck'))
# c=bz2.BZ2Compressor()
# d=''.join(c.compress(str(i)) for i in range(10))
# d+=c.flush()
# print d
# print bz2.decompress(d)