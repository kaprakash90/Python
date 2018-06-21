from IPython.display import clear_output

def display_board(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    player_marker = ''

    while player_marker != 'X' and player_marker != 'O':
        player_marker = input('Player1, which one you wanna play as X or O ?:')

    if player_marker == 'X':
        player1='X'
        player2='O'
    else:
        player1='O'
        player2='X'
    return (player1,player2)


def place_marker(board, marker, position):

    #board.insert(int(position),marker)
    #board.pop(int(position)+1)
    board[int(position)] = marker

def win_check(board, mark):

    return board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == board[9] == mark or board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark or board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark


import random

def choose_first():
    return 'Player '+str(random.randint(1,2))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True

def player_choice(board):
    pl_choice = 0
    while not space_check(board,int(pl_choice)) or int(pl_choice) not in [1,2,3,4,5,6,7,8,9]:
        pl_choice = input('Choose any number from 1-9:')
    return pl_choice

def replay():
    pl_ip = input('So you wanna play again?(y/n):')
    return pl_ip == 'y'

print('Welcome to Tic Tac Toe by Arun!')
while True:
    myboard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(myboard)
    player1_mark, player2_mark = player_input()
    ready = input('Are we ready? y or n?')
    if ready == 'y':
        game_on = True
    else:
        game_on = False
        break

    whose_palyin = choose_first()
    print(str(whose_palyin) +' will go first')

    while game_on:
        if whose_palyin =='Player 1':
            display_board(myboard)
            cosen_num = player_choice(myboard)
            place_marker(myboard, player1_mark, cosen_num)

            if win_check(myboard, player1_mark):
                display_board(myboard)
                print('Player 1 Wins!!!')
                game_on = False
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print('Its a TIE!!!')
                    game_on = False
                else:
                    whose_palyin = 'Player 2'
        else:
            display_board(myboard)
            cosen_num = player_choice(myboard)
            place_marker(myboard, player2_mark, cosen_num)

            if win_check(myboard, player2_mark):
                display_board(myboard)
                print('Player 2 Wins!!!')
                game_on = False
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print('Its a TIE!!!')
                    game_on = False
                else:
                    whose_palyin = 'Player 1'

    if not replay():
        break