import heapq
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]   
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star(start_state):
    pq = []
    heapq.heappush(pq, (heuristic(start_state), 0, start_state, [])) 
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        state_tuple = tuple(tuple(row) for row in state)

        if state == goal_state:
            return path + [state]

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (g+1 + heuristic(neighbor), g+1, neighbor, path + [state]))
    
    return None 
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = a_star(start_state)

if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution exists") 
