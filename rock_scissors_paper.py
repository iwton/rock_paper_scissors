import random
import time

thing = ['paper', 'rock', 'scissors']

a = input('Do you want to play at rock paper scissor?: ')

while a != 'no':
    thing_1 = random.choice(thing)
    thing_2 = input('Enter the word: ').lower()

    print('rock...')
    time.sleep(1)
    print('scissors...')
    time.sleep(1)
    print('''paper!
        ''')

    print('I choose', thing_1, 'you choose', thing_2)
    if thing_1 == 'paper':
        if thing_2 == 'rock':
            print('You lose :(')
        elif thing_2 == 'scissors':
            print('You won!!! :)')
        elif thing_2 == 'paper':
            print('draw!')

    elif thing_1 == 'scissors':
        if thing_2 == 'rock':
            print('You lose :(')
        elif thing_2 == 'scissors':
            print('draw!')
        elif thing_2 == 'paper':
            print('You win!!! :) ')

    elif thing_1 == 'rock':
        if thing_2 == 'rock':
            print('draw!')
        elif thing_2 == 'scissors':
            print('You lose... :(')
        elif thing_2 == 'paper':
            print('You won!!! :)')
    a = input('Do you want to try again?: ')
