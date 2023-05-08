from collections import deque


n, m = map(int, input().split())
matrix = []
path = {}

for i in range(n):
    row = input()
    matrix.append(row)

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
def inbound(n, m, x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(coord):
    # x, y = coord
    fringe = deque([coord])

    while fringe:
        parent = fringe.popleft()
        x, y = parent

        for dx, dy in directions:
            nx, ny = dx + x, dy + y

            if inbound(len(matrix), len(matrix[0]), nx, ny) and matrix[nx][ny] == matrix[x][y] and (nx, ny) not in path:
                fringe.append((nx, ny))
                path[(nx, ny)] = parent
            
            elif inbound(len(matrix), len(matrix[0]), nx, ny) and matrix[nx][ny] == matrix[x][y] and (nx, ny) != path[parent] and (nx, ny) in path:
                return True
    
    return False

cycle = False
for r in range(n):
    if cycle: break

    for c in range(m):
        if (r, c) not in path:
            path[(r, c)] = None 
            if bfs((r, c)):
                cycle = True
                break

if cycle:
    print('Yes')

else:
    print('No')
