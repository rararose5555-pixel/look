from heapq import heappush, heappop

def manhattan_distance(state, goal):

    distance = 0

    for num in range(1, 9):
        x1, y1 = divmod(state.index(num), 3) 
        x2, y2 = divmod(goal.index(num), 3)

        distance += abs(x1-x2) + abs(y1 - y2)

    return distance

def get_neighbors(state):

    neighbors =[]

    zero_pos = state.index(0) 
    x, y = divmod(zero_pos, 3)

    directions =[ (-1, 0) , (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:

        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3: 
            new_zero_pos = nx * 3 + ny

            new_state = list(state)

            new_state[zero_pos], new_state[new_zero_pos] = new_state[new_zero_pos], new_state[zero_pos] 
            neighbors.append(tuple(new_state))

    return neighbors

def a_star(start, goal):

    open_set = [] 
    
    heappush(open_set, (manhattan_distance(start, goal), 0, start, [])) 
    
    visited = set() 

    while open_set:

        f, g, current, path = heappop(open_set)

        if current == goal:
            return path

        if current in visited: 
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):

            if neighbor not in visited: 
                heappush(open_set, ( g + 1 + manhattan_distance(neighbor, goal), g + 1, neighbor, path + [neighbor]))

    return None   

if __name__ == "__main__": 
    start = (1, 3, 5,
             4, 0, 2,
             7, 8, 6)

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    solution = a_star(start, goal)

    if solution:

        print(f"Solution found in {len(solution)} moves!")
        
        print(f"Step 0 (Start):")
        for i in range(0, 9, 3):
            print(start[i:i+3])
        print()

        for step, state in enumerate(solution, 1):

            print(f"Step {step}:")

            for i in range(0, 9, 3):

                print(state[i:i+3])

            print()

    else:

        print("No solution found.")