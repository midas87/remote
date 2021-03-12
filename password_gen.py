# My Password generator

### Start the code on 8th of March 2021 ###
### Finish on 12th of March 2021 12:00 AM ###

#print('***')
#print('--***')
#print('----***''\n')

print('Welcome to my Password Generator''\n')


import random

password = []
listString = ''

myString = 'abcdefghijklmnopqrstuvwxyz'
specialChart = "!@#$%^&*?~"
capString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

maxstringLen = 10


for word in myString:
    if word not in password and len(password) < maxstringLen:
        chk = random.choice(myString)
        password.append(chk)
    if specialChart not in password and len(password) < maxstringLen:
        sChart = random.choice(specialChart)
        password.append(sChart)
    if capString not in password and len(password) < maxstringLen:
        sCap = random.choice(capString)
        password.append(sCap)
    if password != '' and len(password) < maxstringLen:
        intS = random.randint(1,9)
        password.append(intS)

print(password,'\n')
newListString = ''.join([str(item) for item in password])
print('Password:',newListString)
