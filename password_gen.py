# My Password generator

import random

password = []
myString = ''

myString = 'abcdefghijklmnopqrstuvwxyz'
specialChart = "!@#$%^&*?~"
capString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

maxstringLen = 8
stringLen = 4

for word in myString:
    if word not in password and len(password) < maxstringLen:
        chk = random.choice(myString)
        password.append(chk)
        #print(len(password))
    #for n in specialChart:
    if specialChart not in password and len(password) < maxstringLen:
        sChart = random.choice(specialChart)
        password.append(sChart)
    if capString not in password and len(password) < maxstringLen:
        sCap = random.choice(capString)
        password.append(sCap)
    #if password is not ='':

print(password)
