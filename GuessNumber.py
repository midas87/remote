# Number Guess

import random

numb = random.randint(1,20)
#print(numb)

print('You have five guesses')

count = 1
maxCount = 5

#guess = int(input('Guess the number: '))

#print('Guess the number: ', end='')
try:
    guess = int(input('Guess the number: '))
except ValueError:
    print('Please enter number only')

while True:
        try:
            guess = int(input('Guess the number: '))


            if count == maxCount:
                print('you have max your number of guesses, the guess number is:',numb)
                break
            if numb > guess:
                print('You guess is low, Please try again')
                guess = int(input('Guess the number: '))
                count = count + 1

            if numb < guess:
                print('You guess is high, please choose lower number')
                guess = int(input('Guess the number: '))
                count = count + 1

            if numb == guess:
                print('You got the guess right, the correct number is:',numb)
                break
        except ValueError:
            print('Number Only')


#NameError
#ValueError
