# import random library to use random function
import random

# function to display game board


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# function to check win condition


def check_win(board, player):
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                      (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for condition in win_conditions:
        if board[condition[0]-1] == player and board[condition[1]-1] == player and board[condition[2]-1] == player:
            return True
    return False

# function to check if the game is a tie


def check_tie(board):
    if " " not in board:
        return True
    else:
        return False

# function for player move


def player_move(board):
    move = int(input("Enter your move (1-9): "))
    if move < 1 or move > 9:
        print("Invalid move. Please try again.")
        player_move(board)
    elif board[move-1] != " ":
        print("Space already filled. Please try again.")
        player_move(board)
    else:
        board[move-1] = "X"

# function for AI move


def AI_move(board):
    empty_spaces = []
    for i in range(9):
        if board[i] == " ":
            empty_spaces.append(i)
    move = random.choice(empty_spaces)
    board[move] = "O"

# main function to run the game


def run_game():
    board = [" " for x in range(9)]
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if check_win(board, "X"):
            print("You win!")
            break
        elif check_tie(board):
            print("It's a tie!")
            break
        AI_move(board)
        print_board(board)
        if check_win(board, "O"):
            print("AI wins!")
            break
        elif check_tie(board):
            print("It's a tie!")
            break


# start the game
run_game()
