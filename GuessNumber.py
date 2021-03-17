import random

print('Try your luck, Guessing Game')

numb = random.randint(1,20)

print('You have five guesses')

count = 0
maxCount = 5

#guess = int(input('Guess the number: '))

while True:
        try:
            guess = int(input('Guess the number: '))

            if count == maxCount:
                print('you have max your number of guesses, the guess number is:',numb)
                break

            if numb > guess:
                print('You guess is low, Please try again')
                #guess = int(input('Guess the number: '))
                count = count + 1
                countRem = maxCount - count
                print('You have',countRem,'guesses left')

            if numb < guess:
                print('You guess is high, please choose lower number')
                #guess = int(input('Guess the number: '))
                count = count + 1
                countRem = maxCount - count
                print('You have', countRem, 'guesses left')

            if numb == guess:
                print('You got the guess right, the correct number is:',numb)
                break
        except ValueError:
            print('Numbers Only')

