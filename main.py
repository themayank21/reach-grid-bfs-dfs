import time
import reach_bfs as bfs, reach_dfs as dfs


if __name__ == "__main__":
    # Input requires two grid Input and Goal with a blank character 'B'
    # inputGrid and goalGrid of 3x3 tuple matrix
    inputGrid = (
        (3, 2, 1),
        (4, 5, 6),
        (8, 7, 'B')
    )

    goalGrid = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 'B')
    )

    # inputGrid = (
    #     (2, 3, 6),
    #     (1, 5, 'B'),
    #     (4, 7, 8)
    # )

    # goalGrid = (
    #     (1, 2, 3),
    #     (4, 5, 6),
    #     (7, 8, 'B')
    # )

    # counting total steps and time taken by the algorithms - BFS and DFS to reach desired state.
    startTime_bfs = time.time()
    stepCount_bfs = bfs.reachPuzzleGridUsingBFS(inputGrid, goalGrid)
    endTime_bfs = time.time()
    timeDiff_bfs = endTime_bfs - startTime_bfs

    startTime_dfs = time.time()
    stepCount_dfs = dfs.reachPuzzleGridUsingDFS(inputGrid, goalGrid)
    endTime_dfs = time.time()
    timeDiff_dfs = endTime_dfs - startTime_dfs


    print(f"time taken by BFS: {timeDiff_bfs}")
    if stepCount_bfs != -1:
        print(f"BFS will take {stepCount_bfs} steps to reach the goal state.")
    else:
        print("Goal state is not reachable using BFS.")

    print(f"time taken by DFS: {timeDiff_dfs}")
    if stepCount_dfs != -1:
        print(f"DFS will take {stepCount_dfs} steps to reach the goal state.")
    else:
        print("Goal state is not reachable using DFS.")

    if timeDiff_bfs == timeDiff_dfs: 
        print(f"Both algorithm took same amount of time to reach goal state. ")
    elif timeDiff_bfs > timeDiff_dfs:
        print(f"BFS took more time to reach goal state than DFS")
    else:
        print(f"DFS took more time to reach goal state than BFS")

    if stepCount_bfs == stepCount_dfs: 
        print(f"Both algorithm took same amount of steps to reach goal state. ")
    elif stepCount_bfs > stepCount_dfs:
        print(f"BFS took more step count to reach goal state than DFS")
    else:
        print(f"DFS took more step count to reach goal state than BFS")
