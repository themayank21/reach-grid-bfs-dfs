# Convert to Goal state

This Python program demonstrates the Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms to convert a grid in desired state. The task is to reach a goal state grid configuration from a input grid configuration by moving the blank space ('B').

## Problem Description

Given a 3x3 grid containing numbers from 1 to 8 and a blank space ('B'), the task is to move the blank space to reach a target grid configuration. In one step, the blank space can move top, down, left, or right. The target grid configuration is fixed.

### Input

Start Grid:
(
    (3, 2, 1),
    (4, 5, 6),
    (8, 7, 'B')
)

Target Grid: 
(
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 'B')
)

### Output

time taken by BFS: 0.6037964820861816
BFS will take 24 steps to reach the goal state.
time taken by DFS: 0.4650583267211914
DFS will take 103154 steps to reach the goal state.
BFS took more time to reach goal state than DFS
DFS took more step count to reach goal state than BFS

## Code Overview

- `reachPuzzleGridUsingBFS(input_grid, goal_grid)`: Performs Breadth-First Search to find the number of steps required to reach the target grid.
- `reachPuzzleGridUsingDFS(input_grid, goal_grid)`: Performs Depth-First Search to find the number of steps required to reach the target grid.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/themayank21/reach-grid-bfs-dfs.git
cd reach-grid-bfs-dfs