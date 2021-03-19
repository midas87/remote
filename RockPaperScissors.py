#Rock Paper Scissors Game

print('ROCK, PAPER SCISSORS GAME','\n')

import random

compGuess = ['Rock', 'Paper', 'Scissors']


while True:
    try:

        compGuessPick = random.choice(compGuess)

        humanPick = input('Rock, Paper, Scissors, Shoot: ')

        if compGuessPick == 'Rock' and humanPick == 'Rock':
            print('It is a draw, try again ')

        if compGuessPick == 'Rock' and humanPick == 'Scissors':
            print('Rock beats Scissors, Rock wins, Computer Won')
            break

        if compGuessPick == 'Rock' and humanPick == 'Paper':
            print('Paper beats Rock, Paper wins, I won')
            break

        if compGuessPick == 'Paper' and humanPick == 'Rock':
            print('Paper cover rocks, Paper wins, Computer Won')
            break
        if compGuessPick == 'Paper' and humanPick == 'Scissors':
            print('Scissors cut Paper, Scissors wins, I Won')
            break
        if compGuessPick == 'Paper' and humanPick == 'Paper':
            print('It is a Draw, try again')

        if compGuessPick == 'Scissors' and humanPick == 'Scissors':
            print('It is a draw, try again')

        if compGuessPick == 'Scissors' and humanPick == 'Paper':
            print('Scissors cut Paper, Scissors wins, Computer Won')
            break
        elif compGuessPick == 'Scissors' and humanPick == 'Rock':
            print('Rock crush Scissors, Rock wins, I won')
            break


    except ValueError:
        print('No integers')
