n = int(input())

for _ in range(n):
    m, n = map(int, input().split())
    grid = []

    for rowNum in range(m):
        row = input()
        row = [x for x in row]
        grid.append(row)
    
    empty = "."
    stones = "*"
    obstacles = "o"
    
    for rowNum in range(m):
        for colNum in range(n):
            curEl = grid[rowNum][colNum]

            if curEl == stones:
                for rowN in range(rowNum + 1, m):
                    if grid[rowN][colNum] == empty:
                        grid[rowNum][colNum], grid[rowN][colNum] = grid[rowN][colNum], grid[rowNum][colNum]
                    
                    else:
                        break

    for rowNum in range(m):
        row = grid[rowNum]
        row = ''.join(row)
        grid[rowNum] = row
    
    for row in grid:
        print(row)
    
    print()