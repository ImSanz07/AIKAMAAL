def is_valid(state):
   
    missionaries_left, cannibals_left, boat = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    if (missionaries_left < cannibals_left and missionaries_left > 0) or (missionaries_right < cannibals_right and missionaries_right > 0):
        return False
    
    return True

def get_successor(state):
    possible_states = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    moves = []
    missionaries_left, cannibals_left, boat = state

    if boat == 1:
        for move in possible_states:
            missionaries_new = missionaries_left - move[0]
            cannibals_new = cannibals_left - move[1]
            if 0 <= missionaries_new <= 3 and 0 <= cannibals_new <=3 and is_valid((missionaries_new,cannibals_new,0)):
                moves.append((missionaries_new,cannibals_new,0))
            
    else:
        for move in possible_states:
            missionaries_new = missionaries_left + move[0]
            cannibals_new = cannibals_left + move[1]
            if 0 <= missionaries_new <= 3 and 0 <= cannibals_new <=3 and is_valid((missionaries_new,cannibals_new,1)):
                moves.append((missionaries_new,cannibals_new,1))
    
    return moves
def dls(current_state,goal_state,depth_limit,path):
    if depth_limit == 0 and current_state == goal_state:
        return path
    
    elif depth_limit > 0:
        for successor in get_successor(current_state):
            new_state = dls(successor,goal_state,depth_limit-1, path + [successor])
            if new_state:
                return new_state
            
    return None

def iddfs(initial_state,goal_state):

    depth = 0
    while True:
        path = dls(initial_state, goal_state, depth, [initial_state])
        if path:
            return path
        depth += 1

initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

solution = iddfs(initial_state, goal_state)

if solution:
    print("Solution found:")
    for i, state in enumerate(solution):
        print(f"Step {i + 1}: {state}")
else:
    print("No solution found.")
    