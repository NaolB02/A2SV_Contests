from sys import stdin

n, m = map(int, stdin.readline().split())
matrix = [[] for _ in range(n)]

for i in range(n):
    row = stdin.readline()

    for j, sign in enumerate(row):
        matrix[i].append(sign)

        if sign == 'S':
            S = (i, j)
        
        elif sign == 'T':
            T = (i, j)

# check if a cell is crossed out
def check_if_crossed(r, c, char):
    if (char == 'T' and matrix[r][c] == 'S') or (char == 'S' and matrix[r][c] == 'T'):
        print('YES')
        exit()

# function that crosses out rows and columns 
def cross_out(r, c):
    global m, n
    # cross out the cell itself
    char  = matrix[r][c]

    # to the right
    for j in range(c + 1, m):
        cur = matrix[r][j]
        check_if_crossed(r, j, char)
        if cur == '*':
            break
        matrix[r][j] = char
    
    # to the left
    for j in range(c - 1, -1, -1):
        cur = matrix[r][j]
        check_if_crossed(r, j, char)
        if cur == '*':
            break
        matrix[r][j] = char

    # downwards
    for j in range(r + 1, n):
        cur = matrix[j][c]
        check_if_crossed(j, c, char)
        if cur == '*':
            break
        matrix[j][c] = char
    
    # upwards
    for j in range(r - 1, -1, -1):
        cur = matrix[j][c]
        check_if_crossed(j, c, char)
        if cur == '*':
            break
        matrix[j][c] = char

# crossing out the starting and the target row and column
cross_out(S[0], S[1])
cross_out(T[0], T[1])

for i in range(n):
    char = "*"
    for j in range(m):
        check_if_crossed(i, j, char)

        if matrix[i][j] != ".":
            char = matrix[i][j]

for j in range(m):
    char = "*"
    for i in range(n):
        check_if_crossed(i, j, char)

        if matrix[i][j] != ".":
            char = matrix[i][j]

print("NO")
