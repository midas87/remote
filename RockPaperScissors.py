#Rock Paper Scissors Game

import random

compGuess = ['Rock', 'Paper', 'Scissor']

compGuessPick = random.choice(compGuess)

compGuessDic = {'Rock':1, 'Paper':2, 'Scissors':3}

compPick = random.choice(list(compGuessDic.values()))
#compPick = random.choice(compGuessDic.values())

print(compGuessPick)

humanPick = input('Rock, Paper, Scissors, Shoot: ')

humanPickDic = {'Rock':1, 'Paper':2, 'Scissors':3}

dicPick = {}


if compGuessPick == 'Rock' and humanPick == 'Rock':
    print('it is draw, try again ')
if compGuessPick == 'Rock' and humanPick == 'Scissors':
    print('Rock beats Scissors')
if compGuessPick == 'Paper' and humanPick == 'Rock':
    print('Paper wins')
if compGuessPick == 'Rock' and humanPick == 'Paper':
    print('Rock wins')
if compGuessPick == 'Scissors' and humanPick == 'Scissors':
    print('It is a draw, try again')
if compGuessPick == 'Scissors' and humanPick == 'Paper':
    print('Scissors wins')


