
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random, string

#Andhra Pradesh
# font = ImageFont.truetype("ariblk.ttf", 20)
# fontlab = ImageFont.truetype("ariblk.ttf", 25)
# #Data Generation
# for i in range(0,200):
#    img = Image.open("apbp.jpg")
#    draw = ImageDraw.Draw(img)
#    textadd = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(5,20)))
#    for itr in range(random.randint(1,3)):
#        ins_pos=random.randint(0,len(textadd)-2)
#        if textadd[ins_pos]!=" ":
#            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
#        else:
#            itr-=1
#    draw.text((227,128),textadd,(0,0,0),font=font)
#    textadd = ''.join(random.choice(string.ascii_uppercase+ " ") for _ in range(random.randint(5,20)))
#    for itr in range(random.randint(1,3)):
#        ins_pos=random.randint(0,len(textadd)-2)
#        if textadd[ins_pos]!=" ":
#            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
#        else:
#            itr-=1
#    draw.text((227,160),textadd,(0,0,0),font=font)
#    textadd = ''.join(random.choice(string.digits+" "+"\\"+"-") for _ in range(random.randint(5,20)))
#    draw.text((227,188),textadd,(0,0,0),font=font)
#    textadd = ''.join(random.choice(string.ascii_uppercase + string.digits+" ") for _ in range(random.randint(5,20)))
#    draw.text((227,215),textadd,(0,0,0),font=font)
#    for itr in range(random.randint(1,3)):
#        ins_pos=random.randint(0,len(textadd)-2)
#        if textadd[ins_pos]!=" ":
#            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
#        else:
#            itr-=1
#    textadd = ''.join(random.choice(string.ascii_uppercase + string.digits+" ") for _ in range(random.randint(5,20)))
#    draw.text((227,243),textadd,(0,0,0),font=font)
#    for itr in range(random.randint(1,3)):
#        ins_pos=random.randint(0,len(textadd)-2)
#        if textadd[ins_pos]!=" ":
#            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
#        else:
#            itr-=1
#    textadd = ''.join(random.choice(string.ascii_uppercase  + string.digits+" ") for _ in range(random.randint(5,20)))
#    draw.text((227,271),textadd,(0,0,0),font=font)
#    for itr in range(random.randint(1,3)):
#        ins_pos=random.randint(0,len(textadd)-2)
#        if textadd[ins_pos]!=" ":
#            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
#        else:
#            itr-=1
#    textadd = ''.join(random.choice(string.ascii_uppercase + string.digits+" ") for _ in range(random.randint(5,20)))
#    draw.text((227,299),textadd,(0,0,0),font=font)
#    title="ap."+str(i)+'.jpg'
#    for itr in range(random.randint(1,4)):
#        ins_pos=random.randint(0,len(textadd)-2)
#        if textadd[ins_pos]!=" ":
#            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
#        else:
#            itr-=1
#    textadd="AP"
#    for i in range(14):
#        textadd+=str(random.randint(0,9))
#    draw.text((225,101),textadd,(223,103,122),font=fontlab)
#    img.save('AP/'+title)

#Bihar
#font = ImageFont.truetype("arial.ttf", 13)
#for o in range(0,200):
    # img = Image.open("biharbp.jpg")
    # draw = ImageDraw.Draw(img)
    # textadd = ''.join(random.choice(string.ascii_uppercase+" ") for _ in range(random.randint(5,20)))
    # for itr in range(random.randint(1,3)):
    #     ins_pos=random.randint(0,len(textadd)-2)
    #     if textadd[ins_pos]!=" ":
    #         textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
    #     else:
    #         itr-=1
    # draw.text((220,83),textadd,(0,0,0),font=font)
    # textadd = ''.join(random.choice(string.ascii_uppercase+" ") for _ in range(random.randint(5,20)))
    # for itr in range(random.randint(1,3)):
    #     ins_pos=random.randint(0,len(textadd)-2)
    #     if textadd[ins_pos]!=" ":
    #         textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
    #     else:
    #         itr-=1
    # draw.text((220,99),textadd,(0,0,0),font=font)
    # textadd = ''.join(random.choice(string.ascii_uppercase  + string.digits+" ") for _ in range(random.randint(5,20)))
    # for itr in range(random.randint(1,3)):
    #     ins_pos=random.randint(0,len(textadd)-2)
    #     if textadd[ins_pos]!=" ":
    #         textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
    #     else:
    #         itr-=1
    # draw.text((220,112),textadd,(0,0,0),font=font)
    # textadd = ''.join(random.choice(string.ascii_uppercase + string.digits+" ") for _ in range(random.randint(5,20)))
    # for itr in range(random.randint(1,3)):
    #     ins_pos=random.randint(0,len(textadd)-2)
    #     if textadd[ins_pos]!=" ":
    #         textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
    #     else:
    #         itr-=1
    # draw.text((220,128),textadd,(0,0,0),font=font)
    # textadd = ''.join(random.choice(string.ascii_uppercase  + string.digits+" ") for _ in range(5,20))
    # for itr in range(random.randint(1,3)):
    #     ins_pos=random.randint(0,len(textadd)-2)
    #     if textadd[ins_pos]!=" ":
    #         textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
    #     else:
    #         itr-=1
    # draw.text((220,145),textadd,(0,0,0),font=font)
    # textadd =  str(random.randint(1,30))+"-"
    # textadd +=  str(random.randint(1,12))+"-"
    # textadd +=  str(random.randint(1950,2018))
    # draw.text((224,207),textadd,(0,0,0),font=font)
    # textadd = random.choice(["A","B","O","AB"])
    # textadd=textadd+random.choice(["+","-"])
    # draw.text((365,201),textadd,(0,0,0),font=font)
    # textadd="BR-"
    # for i in range(13):
    #     textadd+=str(random.randint(0,9))
    # draw.text((353,62),textadd,(255,255,255),font=font)
    # title="bihar."+str(o)+'.jpg'
    # img.save('Bihar/'+title)


#Madhya Pradesh
font = ImageFont.truetype("ariblk.ttf", 14)
font_1 = ImageFont.truetype("ariblk.ttf", 16)
for o in range(0,200):
    img = Image.open("mpbp.jpg")
    draw = ImageDraw.Draw(img)
    textadd = ''.join(random.choice(string.ascii_uppercase+" ") for _ in range(random.randint(5,10)))
    for itr in range(random.randint(1,3)):
        ins_pos=random.randint(0,len(textadd)-2)
        if textadd[ins_pos]!=" ":
            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
        else:
            itr-=1
    draw.text((287,152),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase+" ") for _ in range(random.randint(5,15)))
    for itr in range(random.randint(1,3)):
        ins_pos=random.randint(0,len(textadd)-2)
        if textadd[ins_pos]!=" ":
            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
        else:
            itr-=1
    draw.text((287,165),textadd,(0,0,0),font=font)

    textadd = ''.join(random.choice(string.ascii_uppercase+" ") for _ in range(random.randint(5,20)))
    for itr in range(random.randint(1,3)):
        ins_pos=random.randint(0,len(textadd)-2)
        if textadd[ins_pos]!=" ":
            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
        else:
            itr-=1
    draw.text((284,193),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase  + string.digits+" ") for _ in range(random.randint(5,20)))
    for itr in range(random.randint(1,3)):
        ins_pos=random.randint(0,len(textadd)-2)
        if textadd[ins_pos]!=" ":
            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
        else:
            itr-=1
    draw.text((288,211),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase + string.digits+" ") for _ in range(random.randint(5,20)))
    for itr in range(random.randint(1,3)):
        ins_pos=random.randint(0,len(textadd)-2)
        if textadd[ins_pos]!=" ":
            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
        else:
            itr-=1
    draw.text((288,225),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase  + string.digits+" ") for _ in range(5,20))
    for itr in range(random.randint(1,3)):
        ins_pos=random.randint(0,len(textadd)-2)
        if textadd[ins_pos]!=" ":
            textadd=textadd[:ins_pos]+" "+textadd[ins_pos:]
        else:
            itr-=1
    draw.text((288,238),textadd,(0,0,0),font=font)
    textadd =  str(random.randint(1,30))+"-"
    textadd +=  str(random.randint(1,12))+"-"
    textadd +=  str(random.randint(1950,2018))
    draw.text((284,293),textadd,(0,0,0),font=font)
    textadd = random.choice(["A","B","O","AB"])
    textadd=textadd+random.choice(["+","-"])
    draw.text((416,295),textadd,(0,0,0),font=font)
    textadd="MP"
    for i in range(2):
        textadd+=str(random.randint(0,9))
    draw.text((280,128),textadd,(0,0,0),font=font)
    textadd = ''.join(random.choice(string.ascii_uppercase+" ") for _ in range(1))
    draw.text((323,128),textadd,(0,0,0),font=font)
    textadd="-"
    draw.text((335,127),textadd,(0,0,0),font=font_1)
    textadd +=  str(random.randint(1950,2018))
    draw.text((338,128),textadd,(0,0,0),font=font)
    textadd="-"
    draw.text((381,127),textadd,(0,0,0),font=font_1)
    textadd = ''.join(random.choice(string.digits+" ") for _ in range(7))
    for itr in range(random.randint(1,3)):
        ins_pos=random.randint(0,len(textadd)-2)
        if textadd[ins_pos]!=" ":
            textadd=textadd[:ins_pos]+textadd[ins_pos:]
        else:
            itr-=1
    draw.text((387,128),textadd,(0,0,0),font=font)
    title="mp."+str(o)+'.jpg'
    img.save('MP/'+title)
