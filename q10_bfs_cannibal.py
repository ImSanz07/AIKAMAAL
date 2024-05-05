from collections import deque

initial_state = (3,3,1)
goal_state = (0,0,0)

def is_valid(state):
    missionaries_left,cannibals_left,boat = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    if missionaries_left < cannibals_left and missionaries_left > 0:
        return False
    if missionaries_right < cannibals_right and missionaries_right > 0:
        return False
    return True

def next_states(state):
    possible_states = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    missionaries_left,cannibals_left,boat = state
    moves = []

    if boat == 1:
        for move in possible_states:
            missionaries_new = missionaries_left - move[0]
            cannibals_new = cannibals_left - move[1]
            if 0 <= missionaries_new <= 3 and 0 <= cannibals_new <= 3 and is_valid((missionaries_new, cannibals_new, 0)):
                moves.append((missionaries_new, cannibals_new, 0))
    else:
        for move in possible_states:
            missionaries_new = missionaries_left + move[0]
            cannibals_new = cannibals_left + move[1]
            if 0 <= missionaries_new <= 3 and 0 <= cannibals_new <= 3 and is_valid((missionaries_new, cannibals_new, 1)):
                moves.append((missionaries_new, cannibals_new, 1))

    return moves

def bfs():
    visited = set()
    queue = deque([(initial_state,[])])

    while queue:
        state,path = queue.popleft()
        visited.add(state)

        if state == goal_state:
            return path

        for new_state in next_states(state):
            if new_state not in visited:
                queue.append((new_state, path + [new_state]) )
                visited.add(new_state)

    return None

solution = bfs()

if solution:
    print("Solution Found")
    for i,state in enumerate(solution):
        print(f"State{i+1}: {state}")

else:
    print("Solution NOT FOUND")