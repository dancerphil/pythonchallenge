# -*- coding: utf-8 -*- 
'''
Created on 2015年10月25日18时13分

@author: dancerphil
'''
dir='11\\'
from PIL import Image
img = Image.open(dir+"11.jpg")

# 1
im1 = Image.new(mode='RGB',size=(img.size[0]/2,img.size[1]/2))
im2 = Image.new(mode='RGB',size=(img.size[0]/2,img.size[1]/2))
im3 = Image.new(mode='RGB',size=(img.size[0]/2,img.size[1]/2))
im4 = Image.new(mode='RGB',size=(img.size[0]/2,img.size[1]/2))
for i in range(img.size[1]):
    for j in range(img.size[0]):
        if i%2==0 and j%2==0:
            im1.putpixel((j/2, i/2), value=img.getdata()[img.size[0]*i+j])
        if i%2==0 and j%2==1:
            im2.putpixel((j/2, i/2), value=img.getdata()[img.size[0]*i+j])
        if i%2==1 and j%2==0:
            im3.putpixel((j/2, i/2), value=img.getdata()[img.size[0]*i+j])
        if i%2==1 and j%2==1:
            im4.putpixel((j/2, i/2), value=img.getdata()[img.size[0]*i+j])
im1.save(dir+'11_out1.png', "PNG")
im2.save(dir+'11_out2.png', "PNG")
im3.save(dir+'11_out3.png', "PNG")
im4.save(dir+'11_out4.png', "PNG")
