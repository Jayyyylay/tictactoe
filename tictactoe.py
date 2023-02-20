def print_board(board):
    """Prints the Tic Tac Toe board"""
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")


def check_win(board, player):
    """Checks if the player has won the game"""
    return ((board[7] == player and board[8] == player and board[9] == player) or
            (board[4] == player and board[5] == player and board[6] == player) or
            (board[1] == player and board[2] == player and board[3] == player) or
            (board[7] == player and board[4] == player and board[1] == player) or
            (board[8] == player and board[5] == player and board[2] == player) or
            (board[9] == player and board[6] == player and board[3] == player) or
            (board[7] == player and board[5] == player and board[3] == player) or
            (board[9] == player and board[5] == player and board[1] == player))


def tic_tac_toe():
    """Main function that plays the game"""
    board = [" "] * 10
    player = "X"
    game_over = False
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while not game_over:
        while True:
            try:
                move = int(input("Player " + player + ", enter a number (1-9): "))
                if move > 9:
                    print("\nPlease input 1-9 integer only!\n")
                else:
                    break
            except ValueError:
                print("\nPlease input 1-9 integer only!\n")

        if board[move] == " ":
            board[move] = player
            print_board(board)
            if check_win(board, player):
                print("Congratulations, Player " + player + " wins!")
                game_over = True
            elif " " not in board:
                print("The game is a tie!")
                game_over = True
            else:
                player = "O" if player == "X" else "X"
        else:
            print("That space is already occupied. Please try again.")


tic_tac_toe()