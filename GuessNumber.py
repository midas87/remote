# Number Guess

import random

numb = random.randint(1,20)

print('You have three guesses')

print('Guess the number: ', end='')

guess = int(input())
count = 0
maxCount = 3

while True:

    if numb > guess:
        print('your guess is low')
        count = count + 1
    elif numb < guess:
        print('your guess is high')
    elif count == maxCount:
        print('You have max you guesses')
    else:
        print('Please try again')
