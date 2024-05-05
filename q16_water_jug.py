def actions(state,jug1_capacity,jug2_capacity):

    possible_actions = []
    jug1,jug2 = state

    possible_actions.append((jug1_capacity,jug2))
    possible_actions.append((jug1,jug2_capacity))
    possible_actions.append((0,jug2))
    possible_actions.append((jug1,0))

    pour = min(jug1,jug2_capacity - jug2)
    possible_actions.append((jug1 - pour,jug2 + pour))
    pour = min(jug2,jug1_capacity - jug1)
    possible_actions.append((jug1 + pour,jug2 - pour))

    return possible_actions

def water_jug_problem(jug1_capacity,jug2_capacity,target):
    initial_state = (0,0)
    visited = set()
    queue = [(initial_state,[])]

    while queue:
       current_state,action_list = queue.pop(0)

       visited.add(current_state)
       if current_state == target:
           return action_list
       
       for action in actions(current_state,jug1_capacity,jug2_capacity):
           if action not in visited:
               queue.append((action,action_list + [action]))

    return None

jug1_capacity = 4
jug2_capacity = 3
target = (0,2)
solution = water_jug_problem(jug1_capacity, jug2_capacity, target)
print("Solution:",solution)
