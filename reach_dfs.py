
# function to count steps to reach desired goal using DFS
def reachPuzzleGridUsingDFS(input_grid, goal_grid, size):
    stack = [(input_grid, 0)]  # Stack of tuples: (current_grid, steps)
    visited = set()

    while stack:
        current_grid, steps = stack.pop()
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
                stack.append((tuple(map(tuple, new_grid)), steps + 1))
    
    return -1  # Target grid not reachable