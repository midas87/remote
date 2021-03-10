# My Password generator

import random

password = []

myString = 'abcdefghijklmnopqrstuvwxyz'
specialChart = "!@#$%^&*()[]{}?~"
capString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

maxstringLen = 8
stringLen = 4

for word in myString:
    if len(word) < stringLen:
        chk = random.choice(myString)

        password.append(chk)
print(password)
