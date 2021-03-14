# My Password generator

### Start the code on 8th of March 2021 ###
### Finish on 12th of March 2021 12:00 AM ###


print('Welcome to Password Generator''\n')

print('Password length: ', end='')

import random

password = []

maxstringLen = int(input())


myString = 'abcdefghijklmnopqrstuvwxyz'
specialChart = "!@#$%^&*?~"
capString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



for word in myString:

    if word not in password and len(password) < int(maxstringLen):
        chk = random.choice(myString)
        password.append(chk)
    if specialChart not in password and len(password) < int(maxstringLen):
        sChart = random.choice(specialChart)
        password.append(sChart)
    if capString not in password and len(password) < int(maxstringLen):
        sCap = random.choice(capString)
        password.append(sCap)
    if password != '' and len(password) < int(maxstringLen):
        intS = random.randint(1,9)
        password.append(intS)


newListString = ''.join([str(item) for item in password])
print('Password:',newListString)
