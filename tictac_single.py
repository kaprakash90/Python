from IPython.display import clear_output
import random

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
    board[int(position)] = marker

def win_check(board, mark):

    return board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == board[9] == mark or board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark or board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark

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
    while True:
        pl_choice = input('Choose any number from 1-9:')
        if 0 < int(pl_choice) <= 9:
            if space_check(board,int(pl_choice)):
                break
            else:
                print('oops that place is occupied alreay!!.. Try again..')
        else:
            print('oops that is notb a valid number!!.. Try again..')
    return pl_choice

def replay():
    pl_ip = input('So you wanna play again?(y/n):')
    return pl_ip == 'y'

def get_closest_available(board, player_mark,freecells):
    j=0
    closeav = []
    for i in board:
        if i == player_mark:
            if j==1:
                closeav += [2,4,5]
            elif j==2:
                closeav += [1,3,5]
            elif j==3:
                closeav += [2,5,6]
            elif j==4:
                closeav += [1,5,7]
            elif j==5:
                closeav += [1,2,3,4,6,7,8,9]
            elif j==6:
                closeav += [9,3,5]
            elif j==7:
                closeav += [4,5,8]
            elif j==8:
                closeav += [7,5,9]
            elif j==9:
                closeav += [8,5,6]
        j +=1
    if len(freecells) > len(closeav):
        return list(set(freecells).intersection(set(closeav)))
    else:
        return list(set(closeav).intersection(set(freecells)))

def win_or_block(board,closecells,mark):
    if len(closecells)>0:
        for i in closecells:
            board[int(i)] = mark
            if win_check(board, mark):
                board[int(i)] = ' '
                return i
            else:
                board[int(i)] = ' '
        return 0
    else:
        return 0

def advpos(board,comp_mark,closecells):
    if len(closecells) >0:
        for i in closecells:
            il = closecells
            ie = il.remove(i)
            for j in il:
                board[int(i)] = comp_mark
                advposition = win_or_block(board,il,comp_mark)
                if advposition !=0:
                    board[int(i)] = ' '
                    return advposition
                else:
                    board[int(i)] = ' '
            return 0
    else:
        return 0


def get_best_position(board, comp_mark, player_mark):
    j=0
    availnums = []
    occupied = []
    for i in board:
        if i == ' ':
            availnums.append(j)
        else:
            if i != '#':
                occupied.append(j)
        j +=1

    if len(occupied)==0 or 5 in availnums:
        return 5
    else:
        closepl = get_closest_available(board,player_mark,availnums)

        closeco = get_closest_available(board,comp_mark,availnums)

        gowin = 0
        goblock = 0
        getadv = 0

        gowin = win_or_block(board,closeco,comp_mark)
        if gowin != 0:
            return gowin

        goblock = win_or_block(board,closepl,player_mark)
        if goblock!= 0:
            return goblock

        getadv = advpos(board,comp_mark,closeco)
        if getadv!= 0:
            return getadv

        try:
            return list(set(closeco).intersection(set(closepl)))[0]
        except IndexError:
            if len(closeco) < 1:
                return closepl[0]
            else:
                return closepl[0]


print('Welcome to Tic Tac Toe by Arun!')
print('The game uses the old numpad design as below.. keep it in mind while choosing the number!')
sampleboard = ['#','1','2','3','4','5','6','7','8','9']
display_board(sampleboard)
while True:
    myboard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_mark, player2_mark = player_input()

    game_on = True

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
            cosen_num = get_best_position(myboard,player2_mark,player1_mark)
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
