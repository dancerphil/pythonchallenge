# -*- coding: utf-8 -*- 
'''
Created on 2015年10月29日20时19分

@author: dancerphil
'''
# init
dir='12\\'
f = open(dir+"evil2.gfx",'rb')

# # step 1
# for i in range(20):
#     for i in range(5):
#         content = f.read(1)
#         c=[]
#         c.append(content)
#         print "{:10}".format(c),
#     print 

# step 2
content = f.read()
for x in xrange(0,5):
    temp = open(dir+'out_%d.%s' % (x,'png'), 'wb')
    temp.write(''.join(content[x::5]))
    temp.close()
f.close()

# interesting
print open(dir+"evil4.jpg",'rb').read()
