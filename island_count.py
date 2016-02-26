def numIslands(grid):
    if not grid:
        return 0
    x = len(grid)
    y = len(grid[0])
    visited = {}
    count = 0

    def dfs(grid,r,c,visited):
        if grid[r][c] ==0:
            if not([r,c] in visited.keys()):
                visited[(r,c)] = 1
            return
        if grid[r][c] == 1:
            visited[(r,c)] = 1
            if not ( r-1 < 0 or (r-1,c) in visited.keys()):
                dfs(grid, r-1,c,visited)
            if not ( r+1 > (len(grid)-1) or (r+1,c) in visited.keys()):
                dfs(grid, r+1,c,visited)
            if not ( c-1 < 0 or (r,c-1) in visited.keys()):
                dfs(grid, 1,c-1,visited)
            if not ( c+1 > (len(grid[0])-1) or (r,c+1) in visited.keys()):
                dfs(grid, r,c+1,visited)
        return

    for r in range(x):
        for c in range(y):

            if grid[r][c] == 0:
                if (r,c) not in visited.keys():
                    visited[(r,c)] = 1
                continue

            if (r,c) in visited.keys():
                continue

            if grid[r][c] == 1 and (r,c) not in visited.keys():
                dfs(grid, r, c, visited)
                count += 1
    return count
print numIslands([(0,0,1,0),(0,1,0,0),(0,0,0,0),(0,1,1,1)])