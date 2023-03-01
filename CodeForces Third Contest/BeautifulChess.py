from collections import Counter

n = int(input())
a = input()

for _ in range(n):
    rcSums = []
    rcDiff = []

    for rowNum in range(8):
        row = input()

        for colNum in range(len(row)):
            if row[colNum] == "#":
                rcSums.append(rowNum + colNum)
                rcDiff.append(rowNum - colNum)
    
    rcSums = Counter(rcSums)
    rcDiff = Counter(rcDiff)

    freq = 0
    for key in rcSums:
        if rcSums[key] > freq:
            diagonalSum = key
            freq = rcSums[key]
    
    freq = 0
    for key in rcDiff:
        if rcDiff[key] > freq:
            diagonalDiff = key
            freq = rcDiff[key]

    bishopRow = (diagonalSum + diagonalDiff) // 2
    bishopCol = diagonalSum - bishopRow

    print(bishopRow + 1, bishopCol + 1)

    if _ != n - 1:
        a = input()
