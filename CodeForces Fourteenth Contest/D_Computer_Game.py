from collections import deque
from sys import stdin

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def inbound(n, x, y):
    return 0 <= x < 2 and 0 <= y < n

def shortestPathBinaryMatrix(grid):
    if grid[0][0] == 1:
        return -1
    
    n = len(grid[0])
    src, dest = (0, 0), (1, n - 1)
    path = {src : None}      
    queue = deque([src])
    goal = None
    
    while queue:
        parent = queue.popleft()
        px, py = parent
        
        if parent == dest:
            goal = parent
            break
        
        for x, y in directions:
            nx, ny = px + x, py + y
            
            if (nx, ny) not in path and inbound(n, nx, ny) and grid[nx][ny] == 0:
                queue.append((nx, ny))
                path[(nx, ny)] = parent
    
    return goal

t = int(stdin.readline())


for _ in range(t):
    n = int(stdin.readline())
    row1 = stdin.readline()
    row2 = stdin.readline()

    grid = []
    r1 = []
    r2 = []
    for c in range(n):
        r1.append(int(row1[c]))
        r2.append(int(row2[c]))

    grid.append(r1)
    grid.append(r2)


    if not shortestPathBinaryMatrix(grid):
        print("NO")
    
    else:
        print("YES")




            
        