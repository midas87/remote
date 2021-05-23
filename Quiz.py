# import random

# The quiz data. Keys are states and values are their capitals,

# capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock'}


pizza = []

print('Type quit when done with your toppings selection!')

while True:

    toppings = input('Please enter you toppings: ')
    if toppings == 'quit':
        break
    pizza.append(toppings)
    print(toppings, 'has been added to your pizza')

print(f'Your toppings order are: {pizza}')
print('Your toppings for your pizza are: {}'.format(pizza))
