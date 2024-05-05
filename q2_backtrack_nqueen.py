import random

def random_solution(n):

    return [random.randint(0, n-1) for _ in range(n)]

def conflicts(queens):

    n = len(queens)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                count += 1
    return count

def solve_n_queens_backtracking(n):

    board = [-1]*n
    solution = []

    def backtrack(row):
        if row == n:
            solution.append(list(board))
            return
        for col in range(n):
            board[row] = col
            if not any(board[i] == col or abs(board[i] - col) == row - i for i in range(n)):
                backtrack(row + 1)

    backtrack(0)
    return solution

# Print a solution

def print_solution(solution):
    n = len(solution)
    for i in range(n):
        print("".join("Q" if j == solution[i] else "." for j in range(n)))

def main():
    n = 8  # Change this value to solve N-Queens for different board sizes
    solutions = solve_n_queens_backtracking(n)
    if solutions:
        print("Number of solutions:", len(solutions))
        print("One of the solutions:")
        print_solution(solutions[0])
    else:
        print("No solutions found.")

if __name__ == "__main__":
    main()
