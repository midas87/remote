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

"""

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

# print(confirmed_users)
'''
while True:
    if unconfirmed_users not in confirmed_users:
        confirmed_users.append(unconfirmed_users)
        # print(confirmed_users)
        break
'''
# Book method

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

# Display all confirmed users.

print('\nThe following users have been confirmed:')

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


