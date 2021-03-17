# Number Guess

import random

numb = random.randint(1,20)

print('You have three guesses')

print('Guess the number: ', end='')

guess = int(input())
count = 0
maxCount = 3


if numb > guess:
    print('You guess is low')
elif numb < guess:
    print('You guess is high')
else:
    print('You got the guess right, the correct number is:',numb)

