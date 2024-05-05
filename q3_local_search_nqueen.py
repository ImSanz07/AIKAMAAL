import random

def random_solution(n):
    return [random.randint(0,n-1) for _ in range(n)]

def conflicts(queens):
    
    n = len(queens)
    count = 0

    for i in range(n):
        for j in range(i+1,n):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                count+=1

    return count

def hill_climbing(n,max_iter = 1000):

    current_solution = random_solution(n)
    current_conflicts = conflicts(current_solution)

    for _ in range(max_iter):

        best_move = None
        best_conflicts = current_conflicts

        if current_conflicts == 0:
            return current_solution

        for i in range(n):
            for j in range(n):
                if j != current_solution[i]:
                    temp_solution = list(current_solution)
                    temp_solution[i] = j
                    temp_conflicts = conflicts(temp_solution)
                    if temp_conflicts < best_conflicts:
                         best_conflicts = temp_conflicts
                         best_move = (i,j)
        if best_move is None:
           return current_solution
        
        i,j = best_move
        current_solution[i] = j
        current_conflicts = best_conflicts

def print_solution(solution):

    for i in range(len(solution)):
        print("".join("Q" if j == solution[i] else "." for j in range(len(solution)) ) )

def main():
    n = 8  # Change this value to solve N-Queens for different board sizes
    solution = hill_climbing(n)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found within the maximum iterations.")

if __name__ == "__main__":
    main()
        
