# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:13:51 2019

@author: hitesh.jonnalagadda
"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random, string

#Andhra Pradesh
font = ImageFont.truetype("ariblk.ttf", 20)
fontlab = ImageFont.truetype("ariblk.ttf", 25)
#Data Generation
for i in range(0,500):
    img = Image.open("input/Capture.jpg")
    draw = ImageDraw.Draw(img)
    textadd = ''.join(random.choice(string.ascii_uppercase+" ") for _ in range(random.randint(5,20)))
    draw.text((227,128),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase+ " ") for _ in range(random.randint(5,20)))
    draw.text((227,160),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase+ string.digits+" ") for _ in range(random.randint(5,20)))
    draw.text((227,188),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase + string.digits+" ") for _ in range(random.randint(5,20)))
    draw.text((227,215),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase + string.digits+" ") for _ in range(random.randint(5,20)))
    draw.text((227,243),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase  + string.digits+" ") for _ in range(random.randint(5,20)))
    draw.text((227,271),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase + string.digits+" ") for _ in range(random.randint(5,20)))
    draw.text((227,299),textadd,(0,0,0),font=font)
    title="out"+str(i)+'.jpg'
    textadd="AP"
    for i in range(14):
        textadd+=str(random.randint(0,9))
    draw.text((225,101),textadd,(223,103,122),font=fontlab)
    img.save('sample_output/'+title)