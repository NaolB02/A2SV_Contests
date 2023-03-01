n, m, k = map(int, input().split())
seats = []

for rowNum in range(n):
    row = input()
    seats.append(row)
    ways = 0

# checking in rows

for rowNum in range(n):
    left = 0
    row = seats[rowNum]

    for right in range(m):
        length = right - left + 1
        if row[right] == ".":

            if length == k:
                ways += 1
                left += 1
        
        else:
            left = right + 1

# checking in columns

for colNum in range(m):
    left = 0

    for right in range(n):
        seat = seats[right][colNum]
        length = right - left + 1

        if seat == ".":

            if length == k:
                ways += 1
                left += 1
        
        else:
            left = right + 1

    
print(ways)