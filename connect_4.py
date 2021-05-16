'''
Connect Four Game with a 6x7 grid.

To-do:
Fix validation for player 2
Ask to reset game when game over



'''

import numpy as np

def create_board():
    board = np.zeros((6,7), dtype = int)
    return board

board = create_board()

play = True

def connect4(board):

    # Check horizontal
    for row in range(6):
        for column in range(3):
            if board[row][column] == board[row][column + 1] == board[row][column + 2] == board[row][column+3] and board[row][column] != 0:
                return board[row][column]
    
    # Check Vertical
    for column in range(7):
        for row in range(3):
            if board[row][column] == board[row + 1][column] == board[row + 2][column] == board[row + 3][column] and board[row][column] != 0:
                return board[row][column]

    # Check Top-Left to Bot-Right
    for row in range(3):
        for column in range(4):
            if board[row][column] == board[row + 1][column + 1] == board[row + 2][column + 2] == board[row + 3][column + 3] and board[row][column] != 0:
                return board[row][column]

    # Check Bot-Left to Top-Right
    for row in range(5, 2, -1):
        for column in range(3):
            if board[row][column] == board[row - 1][column + 1] == board[row - 2][column + 2] == board[row - 3][column + 3] and board[row][column] != 0:
                return board[row][column]

def validate(input):
    if input > 7:
        print('Please enter a number between 1 and 7. ')
    elif input > 1:
        print('Please enter only one number. ')
        


while play:
    
    try:
        player_1 = int(input('(Player 1) Please pick a column: 1 - 7 \n')) 
        for row in range(5, 0, -1):
            if board[row][player_1 - 1] == 0:
                board[row][player_1 - 1] = 1
                break
    except:
        validate(player_1)
        continue

    print(board)
    if connect4(board) == 1:
        print('Congrats! Player 1 wins!')
        break

    try:
        player_2 = int(input('(Player 2) Please pick a column: 1 - 7 \n'))
        for row in range(5, -1, -1):
            if board[row][player_2 - 1] == 0:
                board[row][player_2 - 1] = 2
                break
    except:
        validate(player_2)
        continue            # Need this to return back to player_2 not player_1

    print(board)
    if connect4(board) == 2:
        print('Congrats! Player 2 wins!')
        break

