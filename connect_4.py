# Connect four game: grid: 7x6

import numpy as np

def create_board():
    board = np.zeros((6,7), dtype = int)
    return board

board = create_board()

play = True

def connect4(board):
    
    count1 = 0
    count2 = 0
    # Check horizontal
    while count1 != 4 or count2 != 4:
        for row in range(6):
            for column in range(7):
                if board[row][column] == 1:
                    count1 += 1
                    count2 = 0
                    if count1 == 4:
                        return True
                elif board[row][column] == 2:
                    count2 += 1
                    count1 = 0
                    if count2 == 4:
                        return True
    
    # Check Vertical
    while count1 != 4 or count2 != 4:
        for column in range(6):
            for row in range(7):
                if board[row][column] == 1:
                    count1 += 1
                    count2 = 0
                    if count1 == 4:
                        return True
                elif board[row][column] == 2:
                    count2 += 1
                    count1 = 0
                    if count2 == 4:
                        return True



while play:
    

    player_1 = int(input('Please pick a column: 1 - 7 \n'))
    for row in range(5, 0, -1):
        if board[row][player_1 - 1] == 0:
            board[row][player_1 - 1] = 1

            break

    print(board)

    if connect4(board) == True:
        print('Congrats! Player 1 Wins!')
        break


    





    player_2 = int(input('Please pick a column: 1 - 7 \n'))
    for row in range(5, -1, -1):
        if board[row][player_2 - 1] == 0:
            board[row][player_2 - 1] = 2
            break

    print(board)

    if connect4(board) == True:
        print('Congrats! Player 2 Wins!')
        break
    


