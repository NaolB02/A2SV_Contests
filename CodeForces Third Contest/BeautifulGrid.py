n = int(input())

for _ in range(n):
    size = int(input())
    matrix = []

    for rowNum in range(size):
        row = input()
        listRow = []

        for col in row:
            listRow.append(int(col))
        
        matrix.append(listRow)

    operations = 0
    row = 0
    col = 0
    while size > 1:
        for colNum in range(col, size - 1):
            same = {0 : 0, 1 : 0}
            same[matrix[row][colNum]] += 1
            same[matrix[row][size - 1]] += 1
            same[matrix[size - 1][size - 1 - colNum]] += 1
            same[matrix[size - 1 - colNum][row]] += 1
            print(same, "row:", row, "col:", col, "colNUum:", colNum)
        
            if same[0] == 1 or same[1] == 1:
                operations += 1
            
            elif same[0] == 2:
                operations += 2
            
        row += 1
        col += 1
        size -= 1
    
    print(operations)