"""
f = open('grade.txt', 'r')
newFile = open('pass.text', 'w')
failFile = open('fail.text', 'w')

#count = 1

for check in f:
    checkline = check.split()
    # print(checkline)
    if checkline[2] == 'P':
        newFile.write(check)
    else:
        failFile.write(check)

f.close()
newFile.close()
failFile.close()

"""

print('Welcome To The Movie Theatre...Where Entertainment is your friend!')

child_ticket = 3
teenager_ticket = 12

while True:
    age = int(input('Please enter your age: '))
    if age <= child_ticket:
        print('You get free movie')
        break
    if child_ticket < age <= teenager_ticket:
        print('Your ticket price is $10')
        break
    else:
        print('Your ticket price is $15')
        break


# Writing an Endless loop for Test.

# while True:
    # print('This is an endless loop running!!!')
