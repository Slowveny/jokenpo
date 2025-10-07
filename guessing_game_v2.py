
from random import randint

print(f'{' GUESSING GAME ':=^50}')

while True:
    level = int(input('''Choose the difficulty level:
[ 1 ] Easy
[ 2 ] Medium
[ 3 ] Hard
Chosen level: '''))
    attempts = 0

    if level == 1:
        number = randint(1, 10)
        guess = int(input('Try to guess the number I thought of (from 1 to 10): '))
    elif level == 2:
        number = randint(1, 50)
        guess = int(input('Try to guess the number I thought of (from 1 to 50): '))
    elif level == 3:
        number = randint(1, 100)
        guess = int(input('Try to guess the number I thought of (from 1 to 100): '))
    else:
        print('Invalid mode. Please, try again!')
        continue  # added to restart if mode is invalid

    attempts += 1  

    if level in [1, 2, 3]:
        while guess != number:
            if guess > number:
                print('Your guess was ABOVE the number I thought of.')
            elif guess < number:
                print('Your guess was BELOW the number I thought of.')
            guess = int(input('Wrong number! Try again: '))
            attempts += 1

        print(f'* You GOT IT! I was thinking of the number {number}')
        print(f'* Number of attempts: {attempts}')

        again = input('Would you like to play again (y/n)? ').lower()
        while again not in ['y', 'n']:
            print('Maybe you typed it wrong. Try again.')
            again = input('Would you like to play again (y/n)? ').lower()

        if again == 'n':
            print('Thanks for playing!')
            break