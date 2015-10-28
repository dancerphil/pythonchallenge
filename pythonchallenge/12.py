# -*- coding: utf-8 -*- 
'''
Created on 2015年10月25日23时18分

@author: dancerphil
'''
from PIL import Image
img = Image.open("12.jpg")

# 1
im1 = Image.new(mode='RGB',size=(img.size[0],img.size[1]))
for i in range(img.size[1]):
    for j in range(img.size[0]):
        if j%2==0 and i%6==0:
            im1.putpixel((j/2, i/6), value=img.getdata()[img.size[0]*i+j])
im1.save('12_out1.png', "PNG")
