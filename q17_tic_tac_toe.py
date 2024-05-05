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
     best_value = -float("inf")

     for i in range(9):
          if board[i] == EMPTY:
               board[i] = O
               value = sum(MAGIC_SQUARE[j] for j in range(9) if board[j] == O)
               board[i] = EMPTY

               if i == 4:
                  value += 10
               
               if value > best_value:
                    best_value = value
                    best_move = i
               
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