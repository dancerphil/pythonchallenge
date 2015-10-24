# -*- coding: utf-8 -*- 
'''
Created on 2015年10月25日00时12分

@author: dancerphil
'''
# init
from PIL import Image
img = Image.open("oxygen.png")

# # step 1
# print img.size
# s=''
# for i in range(img.size[1]):
#     for j in range(img.size[0]):
#         s+=chr(img.getdata()[629*i+j][0])
#     s+='\n'
# print s

# step 2
# # 1
# area = (0, 43, 608, 44)
# cut = img.crop(area)
# pixels = cut.getdata()
# s=''
# for i in range(0,len(pixels),7):
#     s += chr(pixels[i][0])# actually it is the red data
# print s

# # 2
# area = (0, 43, 608, 44)
# pixels = img.crop(area).getdata()
# print ''.join(chr(pixels[i][0]) for i in range(0, len(pixels), 7))

# 3
area = (0, 43, 608, 44)
lpixels = img.crop(area).convert('L').getdata()# L data
print ''.join(chr(lpixels[i]) for i in range(0, len(lpixels), 7))

# step 3
result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(chr(x) for x in result)