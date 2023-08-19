import time
import reach_bfs as bfs, reach_dfs as dfs
import random

def generateRandomGrid(n):
    numbers = list(range(1, n*n))
    random.shuffle(numbers)
    numbers.append('B')
    return (tuple(map(tuple, [numbers[i:i+n] for i in range(0, n*n, n)])))

def generateTargetGrid(n):
    numbers = list(range(1, n*n))
    numbers.append('B')
    return (tuple(map(tuple, [numbers[i:i+n] for i in range(0, n*n, n)])))

if __name__ == "__main__":
    # Input requires two grid Input and Goal with a blank character 'B'
    # inputGrid and goalGrid of 3x3 tuple matrix
    # matrix_size is the size of row matrix 

    matrix_size = 2 # matrix of size 3x3
    inputGrid = generateRandomGrid(matrix_size)
    print(inputGrid)
    goalGrid = generateTargetGrid(matrix_size)
    print(goalGrid)

    # counting total steps and time taken by the algorithms - BFS to reach desired state.
    startTime_bfs = time.time()
    stepCount_bfs = bfs.reachPuzzleGridUsingBFS(inputGrid, goalGrid, matrix_size)
    endTime_bfs = time.time()
    timeDiff_bfs = endTime_bfs - startTime_bfs

    # counting total steps and time taken by the algorithms - DFS to reach desired state.
    startTime_dfs = time.time()
    stepCount_dfs = dfs.reachPuzzleGridUsingDFS(inputGrid, goalGrid, matrix_size)
    endTime_dfs = time.time()
    timeDiff_dfs = endTime_dfs - startTime_dfs


    # Printing results
    # Time and steps takes by BFS
    print(f"time taken by BFS: {timeDiff_bfs}")
    if stepCount_bfs != -1:
        print(f"BFS will take {stepCount_bfs} steps to reach the goal state.")
    else:
        print("Goal state is not reachable using BFS.")

    # Time and steps taken by DFS
    print(f"time taken by DFS: {timeDiff_dfs}")
    if stepCount_dfs != -1:
        print(f"DFS will take {stepCount_dfs} steps to reach the goal state.")
    else:
        print("Goal state is not reachable using DFS.")

    # Time comparison between BFS and DFS
    if timeDiff_bfs == timeDiff_dfs: 
        print(f"Both algorithm took same amount of time to reach goal state. ")
    elif timeDiff_bfs > timeDiff_dfs:
        print(f"BFS took more time to reach goal state than DFS")
    else:
        print(f"DFS took more time to reach goal state than BFS")

    # Step comparison between BFS and DFS
    # In case of -1 it is not possible to reach to target state
    if stepCount_bfs == -1 and stepCount_dfs == -1:
        print(f"Both algorithm failed to reach goal state.")
    elif stepCount_bfs == stepCount_dfs: 
        print(f"Both algorithm took same amount of steps to reach goal state. ")
    elif stepCount_bfs > stepCount_dfs:
        print(f"BFS took more step count to reach goal state than DFS")
    else:
        print(f"DFS took more step count to reach goal state than BFS")
