import random

print(f'{' JOKENPO ':=^50}')
moves = ['Rock', 'Paper', 'Scissors']

while True:
    computer_move = random.choice(moves)
    player_move = input('Enter your move (Rock/Paper/Scissors): ').capitalize().strip()
    while player_move not in moves:
        print('Invalid move. Try again!')
        player_move = input('Enter your move (Rock/Paper/Scissors): ').capitalize().strip()

    print(f'Computer chose: {computer_move}')
    if computer_move == player_move:
        print("It's a TIE!")
    else:
        if computer_move == 'Rock':
            if player_move == 'Paper':
                print('You WON!')
            else:
                print('You LOST!')
        elif computer_move == 'Paper':
            if player_move == 'Scissors':
                print('You WON!')
            else:
                print('You LOST!')
        else:
            if player_move == 'Rock':
                print('You WON!')
            else:
                print('You LOST!')

    play_again = input('Do you want to play again? (y/n): ').lower()
    while play_again not in ['y', 'n']:
        play_again = input('Do you want to play again? (y/n): ').lower()
    if play_again == 'n':
        break

print('Thanks for playing!')
