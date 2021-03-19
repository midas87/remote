#Rock Paper Scissors Game

import random

compGuess = ['Rock', 'Paper', 'Scissors']

#compGuessPick = random.choice(compGuess)

compGuessDic = {'Rock':1, 'Paper':2, 'Scissors':3}

compPick = random.choice(list(compGuessDic.values()))
#compPick = random.choice(compGuessDic.values())

#print(compGuessPick)



humanPickDic = {'Rock':1, 'Paper':2, 'Scissors':3}

dicPick = {}

while True:
    try:

        compGuessPick = random.choice(compGuess)

        humanPick = input('Rock, Paper, Scissors, Shoot: ')

        if compGuessPick == 'Rock' and humanPick == 'Rock':
            print('it is draw, try again ')

        if compGuessPick == 'Rock' and humanPick == 'Scissors':
            print('Rock beats Scissors, computer Won')
            break
        if compGuessPick == 'Paper' and humanPick == 'Rock':
            print('Paper wins, computer Won')
            break
        if compGuessPick == 'Rock' and humanPick == 'Paper':
            print('Rock wins, Computer Won')
            break
        if compGuessPick == 'Scissors' and humanPick == 'Scissors':
            print('It is a draw, try again')
            break
        if compGuessPick == 'Scissors' and humanPick == 'Paper':
            print('Scissors wins')
            break
        elif compGuessPick == 'Scissors' and humanPick == 'Rock':
            print('Rock wins')
            break
        elif compGuessPick == 'Scissors' and humanPick == 'Paper':
            print('Scissors wins')
            break
        elif compGuessPick == "Paper" and humanPick == 'Scissors':
            print('Scissors wins')
            break
        if compGuessPick == 'Paper' and humanPick == 'Paper':
            print('It is a Draw, try again')
    except ValueError:
        print('No integers')
