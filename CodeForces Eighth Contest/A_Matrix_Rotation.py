n = int(input())

for _ in range(n):
    matrix = []
    row1 = list(map(int, input().split()))
    matrix.append(row1)

    row2 = list(map(int, input().split()))
    matrix.append(row2)

    isBeautifyable = False
    isBeautiful = matrix[0][0] < matrix[0][1] and matrix[0][0] < matrix[1][0] and matrix[0][1] < matrix[1][1] and matrix[1][0] < matrix[1][1]

    if isBeautiful:
        isBeautifyable = True
        print("YES")
    
    for _ in range(3):
        matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1] = matrix[0][1], matrix[1][1], matrix[0][0], matrix[1][0]
        
        isBeautiful = matrix[0][0] < matrix[0][1] and matrix[0][0] < matrix[1][0] and matrix[0][1] < matrix[1][1] and matrix[1][0] < matrix[1][1]

        if isBeautiful:
            isBeautifyable = True
            print("YES")
            break
    

    if not isBeautifyable:
        print("NO")