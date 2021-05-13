# Connect four game: grid: 7x6

import numpy as np

def create_board():
    board = np.zeros((6,7), dtype = int)
    return board

board = create_board()

play = True

def connect4(arr):
    for row in range(6):

while play:

    player_1 = int(input('Please pick a column: 1 - 7 \n'))
    for row in range(5, 0, -1):
        if board[row][player_1] == 0:
            board[row][player_1] = 'X'
            break
    print(board)



    player_2 = int(input('Please pick a column: 1 - 7 \n'))
    for row in range(5, -1, -1):
        if board[row][player_1] == 0:
            board[row][player_1] = 'O'
            break
    print(board)

