import claptcha
import random
charList = ['A','B','C','D','E','F','G','H','K','P','0','1','2','3','4','5','6','7','8','9']
FIXED_LEN = 4

def generateRandText():
    randText = str()
    for i in range(0,FIXED_LEN):
        randText += charList[random.randint(0,len(charList)-1)]
    return randText


for i in range(0,50):
    mstr = generateRandText()
    c = Claptcha(mstr, "FreeMono.ttf",size=(400,100))

    text, image = c.image
    text, bytes = c.bytes

    text, file = c.write('datasetnew3/'+mstr+'.png')
    print(str(i)+"--> File "+mstr+". png created")
