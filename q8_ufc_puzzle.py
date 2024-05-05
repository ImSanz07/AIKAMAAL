import heapq
import copy

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None, cost=0):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def find_blank_pos(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def possible_actions(blank_pos):
    actions = []
    x, y = blank_pos
    if x > 0:
        actions.append('U')
    if x < 2:
        actions.append('D')
    if y > 0:
        actions.append('L')
    if y < 2:
        actions.append('R')
    return actions

def result(puzzle, action):
    blank_pos = find_blank_pos(puzzle)
    x, y = blank_pos
    new_puzzle = copy.deepcopy(puzzle)
    if action == 'U':
        new_puzzle[x][y], new_puzzle[x - 1][y] = new_puzzle[x - 1][y], new_puzzle[x][y]
    elif action == 'D':
        new_puzzle[x][y], new_puzzle[x + 1][y] = new_puzzle[x + 1][y], new_puzzle[x][y]
    elif action == 'L':
        new_puzzle[x][y], new_puzzle[x][y - 1] = new_puzzle[x][y - 1], new_puzzle[x][y]
    elif action == 'R':
        new_puzzle[x][y], new_puzzle[x][y + 1] = new_puzzle[x][y + 1], new_puzzle[x][y]
    return new_puzzle

def is_goal(puzzle):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return puzzle == goal_state

def uniform_cost_search(initial_state):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, initial_state)

    while priority_queue:
        current_state = heapq.heappop(priority_queue)
        if is_goal(current_state.puzzle):
            return current_state

        visited.add(tuple(map(tuple, current_state.puzzle)))

        blank_pos = find_blank_pos(current_state.puzzle)
        actions = possible_actions(blank_pos)
        for action in actions:
            new_puzzle = result(current_state.puzzle, action)
            if tuple(map(tuple, new_puzzle)) not in visited:
                new_cost = current_state.cost + 1
                new_state = PuzzleState(new_puzzle, current_state, action, new_cost)
                heapq.heappush(priority_queue, new_state)

    return None

def print_solution(state):
    path = []
    while state:
        path.append((state.move, state.puzzle))
        state = state.parent
    path.reverse()
    
    for move, puzzle in path:
        print("Move:", move)
        for row in puzzle:
            print(row)
        print()

# Example usage
initial_puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
initial_state = PuzzleState(initial_puzzle)
goal_state = uniform_cost_search(initial_state)

if goal_state:
    print("Solution found:")
    print_solution(goal_state)
else:
    print("No solution found.")
