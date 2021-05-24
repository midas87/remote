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
'''

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

# Display all confirmed users.

print('\nThe following users have been confirmed:')

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

'''

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# print(pets)
'''

while pets:
    pets.remove('cat')
    if 'cat' not in pets:
        break

print(pets)

# This is much better way to write a code

while 'cat' in pets:
    pets.remove('cat')

print(pets)

'''

'''
# Mountain Poll Code

responses = {}

# Set a flag to indicate that polling is active.

polling_active = True

while polling_active:
    name = input('What is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    # store the response in a dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes/ no) ')
    if repeat == 'no':
        polling_active = False

    # Polling is complete, Show the results.
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f'{name} would like to climb {response}.')


'''

# Sandwich Code

sandwich_orders = ['tortas', 'panini', 'grilled cheese', 'blt sandwich', 'club sandwich,',
                   'piadina romagnola', 'reuben', 'submarine sandwich', 'croque monsieur',
                   'banhmi', 'Po Boy', 'tuna', 'francesinha', 'cheesesteak', 'cuban', 'pastrami']

finished_sandwiches = []

new_sandwich = 'pastrami'


print(sandwich_orders)
print(len(sandwich_orders))

for check in sandwich_orders:

    if len(sandwich_orders) < 18:
        sandwich_orders.append(new_sandwich)

print(sandwich_orders)

if len(sandwich_orders) == 18:
    print('Deli has ran out of Pastrami sandwich')

while sandwich_orders:
    new_sliceSand = sandwich_orders.pop()
    if 'pastrami' not in new_sliceSand:
        finished_sandwiches.append(new_sliceSand.title())


print(f'Here are the finish orders of sandwiches {finished_sandwiches}')
print(len(finished_sandwiches))


'''
for sandwich_order in sandwich_orders:
    print(f'I made your {sandwich_order.title()} sandwich')
    finished_sandwiches.append(sandwich_order)

print('This are the list of sandwich that are made! ')
print(finished_sandwiches)
'''