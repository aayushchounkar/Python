# import numpy as np
# import random
# from time import sleep
 
# # Creates an empty board
 
 
# def create_board():
#     return(np.array([[0, 0, 0],
#                      [0, 0, 0],
#                      [0, 0, 0]]))
 
# # Check for empty places on board
 
 
# def possibilities(board):
#     l = []
 
#     for i in range(len(board)):
#         for j in range(len(board)):
 
#             if board[i][j] == 0:
#                 l.append((i, j))
#     return(l)
 
# # Select a random place for the player
 
 
# def random_place(board, player):
#     selection = possibilities(board)
#     current_loc = random.choice(selection)
#     board[current_loc] = player
#     return(board)
 
# # Checks whether the player has three
# # of their marks in a horizontal row
 
 
# def row_win(board, player):
#     for x in range(len(board)):
#         win = True
 
#         for y in range(len(board)):
#             if board[x, y] != player:
#                 win = False
#                 continue
 
#         if win == True:
#             return(win)
#     return(win)
 
# # Checks whether the player has three
# # of their marks in a vertical row
 
 
# def col_win(board, player):
#     for x in range(len(board)):
#         win = True
 
#         for y in range(len(board)):
#             if board[y][x] != player:
#                 win = False
#                 continue
 
#         if win == True:
#             return(win)
#     return(win)
 
# # Checks whether the player has three
# # of their marks in a diagonal row
 
 
# def diag_win(board, player):
#     win = True
#     y = 0
#     for x in range(len(board)):
#         if board[x, x] != player:
#             win = False
#     if win:
#         return win
#     win = True
#     if win:
#         for x in range(len(board)):
#             y = len(board) - 1 - x
#             if board[x, y] != player:
#                 win = False
#     return win
 
# # Evaluates whether there is
# # a winner or a tie
 
 
# def evaluate(board):
#     winner = 0
 
#     for player in [1, 2]:
#         if (row_win(board, player) or
#                 col_win(board, player) or
#                 diag_win(board, player)):
 
#             winner = player
 
#     if np.all(board != 0) and winner == 0:
#         winner = -1
#     return winner
 
# # Main function to start the game
 
 
# def play_game():
#     board, winner, counter = create_board(), 0, 1
#     print(board)
#     sleep(2)
 
#     while winner == 0:
#         for player in [1, 2]:
#             board = random_place(board, player)
#             print("Board after " + str(counter) + " move")
#             print(board)
#             sleep(2)
#             counter += 1
#             winner = evaluate(board)
#             if winner != 0:
#                 break
#     return(winner)
 
 
# # Driver Code
# print("Winner is: " + str(play_game()))
# Hangup (SIGHUP)
# Traceback (most recent call last):
#   File "Solution.py", line 5, in <module>
#     import numpy as np
# ModuleNotFoundError: No module named 'numpy'
#************************GEEKS FOR GEEKS*****************************


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(len(board))) or \
       all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[i][len(board)-1-i] != ' ' for i in range(len(board))):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(len(board)) for j in range(len(board[0])))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        # Get the player's move
        while True:
            try:
                row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
                col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Make the move
        board[row][col] = current_player

        # Check for a winner or a draw
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
#else:
#    print("game over")