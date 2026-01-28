# 1. Create a 3x3 board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# 6. Check if the game is won
def check_winner(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# 5. Check if the game is a draw
def check_draw():
    return " " not in board

# Game start
current_player = "X"
game_over = False

print("Welcome to Tic Tac Toe")
print("Player 1 = X, Player 2 = O")

# 4. Check if the game is over
while not game_over:
    print_board()
    
    # 2. Take input from players
    move = input(f"Player {current_player}, enter position (1-9): ")

    # 3. Check if input is valid
    if not move.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    move = int(move) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move! Try again.")
        continue

    # Place the move
    board[move] = current_player

    # Check winner
    if check_winner(current_player):
        print_board()
        print(f"🎉 Player {current_player} wins!")
        game_over = True

    # Check draw
    elif check_draw():
        print_board()
        print("🤝 It's a draw!")
        game_over = True

    # Switch player
    else:
        current_player = "O" if current_player == "X" else "X"

# 11. Print game over message
print("Game Over!")