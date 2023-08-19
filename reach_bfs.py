from collections import deque

# function to count steps to reach desired goal state using BFS
def reachPuzzleGridUsingBFS(input_grid, goal_grid, size):
    queue = deque([(input_grid, 0)])  # Queue of tuples: (current_grid, steps)
    visited = set()
    
    while queue:
        current_grid, steps = queue.popleft()
        if current_grid == goal_grid:
            return steps
        
        if current_grid in visited:
            continue
        
        visited.add(current_grid)
        
        # Find the position of 'B' (blank space)
        b_row, b_col = None, None
        for row in range(size):
            for col in range(size):
                if current_grid[row][col] == 'B':
                    b_row, b_col = row, col
                    break
        
        # Possible moves: top, down, left, right
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for row, col in moves:
            new_row, new_col = b_row + row, b_col + col
            if 0 <= new_row < size and 0 <= new_col < size:
                new_grid = [list(row) for row in current_grid]
                new_grid[b_row][b_col], new_grid[new_row][new_col] = new_grid[new_row][new_col], new_grid[b_row][b_col]
                queue.append((tuple(map(tuple, new_grid)), steps + 1))
    
    return -1  # Target grid not reachable