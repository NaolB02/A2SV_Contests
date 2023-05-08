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
    while size - row - 1 >= 0:
        for colNum in range(col, size - 1):
            same = {0 : 0, 1 : 0}
            same[matrix[row][colNum]] += 1
            same[matrix[colNum][-1 - row]] += 1
            same[matrix[-1 - row][-1 - colNum]] += 1
            same[matrix[-1 - colNum][row]] += 1
        
            if len(same) != 1 and same[0] == 1 or same[1] == 1:
                operations += 1
            
            elif same[0] == 2:
                operations += 2
            
        row += 1
        col += 1
        size -= 1
    
    print(operations)