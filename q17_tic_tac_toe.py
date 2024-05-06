EMPTY = '-'
X = 'X'
O = 'O'
MAGIC_SQUARE = [8,3,4,1,5,7,6,9,2]

WINNING_COMBINATIONS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def main():
    board = [EMPTY]*9
    current_player = X
    winner  = None
    while winner is None:
         print_board(board)
         if current_player == X:
              move = get_player_move(board)
              board[move] = X

         else:
              move = get_computer_move(board)
              board[move] = O

         winner = check_winner(board)
         current_player = O if current_player == X else  X

    if winner == X:
         print("X wins!")
    elif winner == O:
         print("O wins!")
    else:
         print("It's a Draw!")

def get_player_move(board):
     while True:
        try:
            choice = int(input("Enter ur choice (0-8):"))
            if 0 <= choice <= 8 and board[choice] == EMPTY:
                 return choice
            else:
                 print("Invalid choice. Try again.")
        
        except ValueError:
            print("Invalid choice. Try again.")

def get_computer_move(board):
    best_move = None
    best_value = -float('inf')  # Initialize to negative infinity

    for i in range(9):
        if board[i] == EMPTY:
            # Check if the move leads to a win for the computer
            board[i] = O
            if check_winner(board) == O:
                board[i] = EMPTY
                return i
            board[i] = EMPTY

            # Check if the move blocks the player from winning
            board[i] = X
            if check_winner(board) == X:
                board[i] = EMPTY
                return i
            board[i] = EMPTY

            # Calculate the value of the move using the Magic Square
            board[i] = O
            move_value = sum(MAGIC_SQUARE[j] for j in range(9) if board[j] == O)
            board[i] = EMPTY  # Reset the board

            # Prioritize center and corners for the computer
            if i == 4:
                move_value += 10  # Center has a higher priority

            # Update the best move if this move is better
            if move_value > best_value:
                best_move = i
                best_value = move_value

    return best_move


def check_winner(board):
     
     for combination in WINNING_COMBINATIONS:
          if all(board[move] == X for move in combination):
               return X
          if all(board[move] == O for move in combination):
               return O
          
     if all(board[i] != EMPTY for i in range(9)):
          return 'DRAW'
     
     return None
def print_board(board):
     
     print(f"{board[0]} | {board[1]} | {board[2]}")
     print("-" *9)
     print(f"{board[3]} | {board[4]} | {board[5]}")
     print("-" *9)
     print(f"{board[6]} | {board[7]} | {board[8]}")
     print("-" *9)

if __name__ == "__main__":
     main()
