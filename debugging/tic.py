#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there is a winner in the game.

    Returns:
        str: The winner ('X' or 'O'), or None if there is no winner.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    """
    Checks if the board is completely filled.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Main function to play the Tic Tac Toe game.
    """
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Input validation
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter a number between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            continue

        # Check if the cell is already occupied
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()

