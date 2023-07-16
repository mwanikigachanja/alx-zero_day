def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X  |  Player 2: O")
    print("The board is numbered as follows:")

    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    player = "X"

    while True:
        print_board(board)

        move = input(f"Player {player}, enter the number (1-9) where you want to place your {player}: ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        move = int(move) - 1
        row, col = divmod(move, 3)

        if board[row][col] != "X" and board[row][col] != "O":
            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Congratulations! Player {player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe_game()

