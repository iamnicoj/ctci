def robot_in_a_grid(grid):

    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return []

    return _dynamic_transvertion(grid, 0, 0, len(grid) - 1 , len(grid[0]) - 1, {})

def _dynamic_transvertion(grid, x, y, len_x, len_y, memo):
    if memo.get(str(x)+':'+ str(y), None) is not None:
        return memo[str(x)+':'+ str(y)]
    if grid[x][y] != 1: 
        memo[str(x)+':'+ str(y)] = []         
        return []
    if x == len_x and y == len_y:
        return [(x,y)]
    
    if y < len_y:
        right = _dynamic_transvertion(grid, x, y + 1, len_x, len_y, memo)
        if len(right) > 0:
            return [(x,y)] + (right[::])
    if x < len_x:
        left = _dynamic_transvertion(grid, x + 1, y, len_x, len_y, memo)
        if len(left) > 0:
            return [(x,y)] + (left[::])
    
    memo[str(x)+':'+ str(y)] = []         
    return []


# WATCH BOTTOM X & Y IS NOT REACHABLE = [] 

grid = [[]]
print(robot_in_a_grid(grid)) # []

grid = [[1]]
print(robot_in_a_grid(grid)) # [(0,0)]


grid = [[1, 1]]
print(robot_in_a_grid(grid)) # [(0,0), (0, 1)]

grid = [[1, 1],[0,1]]
print(robot_in_a_grid(grid)) # [(0,0), (0, 1), (1,1)]

grid = [[1, 1, 1],[0, 1, 1]]
# [(0,0), (0, 1), (0,2), (1,2)] or 
# [(0,0), (0, 1), (1,1), (1,2)]
print(robot_in_a_grid(grid)) 

grid = [[1, 1, 1],[0, 1, 1],[1, 1, 1],[1, 0, 1],[1, 1, 1],[1, 1, 1]]
# [(0,0), (0, 1), (0,2), (1,2)] or 
# [(0,0), (0, 1), (1,1), (1,2)]
print(robot_in_a_grid(grid)) 

grid = [[1, 1, 1],[0, 1, 1],[1, 1, 1],[1, 0, 1],[1, 1, 0],[1, 1, 1]]
# [(0,0), (0, 1), (0,2), (1,2)] or 
# [(0,0), (0, 1), (1,1), (1,2)]
print(robot_in_a_grid(grid)) 
