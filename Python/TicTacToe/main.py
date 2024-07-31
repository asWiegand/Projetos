from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(' ' + board[7]+ ' | ' + board[8]+ ' | '+ board[9])
    print('-----------')
    print(' ' + board[4]+ ' | ' + board[5]+ ' | '+ board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | '+ board[3])

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, escolha X or O: ').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return (((board[7] == marker) and (board[8] == marker) and (board[9] == marker)) or
            ((board[4] == marker) and (board[5] == marker) and (board[6] == marker)) or
            ((board[1] == marker) and (board[2] == marker) and (board[3] == marker)) or
            ((board[7] == marker) and (board[5] == marker) and (board[3] == marker)) or
            ((board[1] == marker) and (board[5] == marker) and (board[9] == marker)) or
            ((board[1] == marker) and (board[4] == marker) and (board[7] == marker)) or
            ((board[2] == marker) and (board[5] == marker) and (board[8] == marker)) or
            ((board[3] == marker) and (board[6] == marker) and (board[9] == marker)))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False

    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Escolha sua jogada (1-9) ' + turn)

    return int(position)

def replay():
    return input('Deseja jogar novamente? [S/N] ').lower().startswith('s')

print('Jogo da Velha')
print('-------------')

turn = choose_first()

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    print(turn+' começa!')

    game_on = True

    while game_on:
        if turn == 'Player 1':
            print('Turno Player 1')
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
        if win_check(board, player1_marker):
            display_board(board)
            print('Player 1 Ganhou!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empatou!')
                break
            else:
                turn = 'Player 2'


        if turn == 'Player 2':
            print('Turno Player 2')
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

        if win_check(board, player2_marker):
            display_board(board)
            print('Player 2 Ganhou!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empatou!')
                break
            else:
                turn = 'Player 1'

    if not replay():
        break