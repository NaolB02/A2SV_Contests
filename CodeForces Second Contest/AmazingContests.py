n = int(input())

points = list(map(int, input().split()))
amazing = 0

for index, point in enumerate(points):
    if index == 0:
        minpt = point
        maxpt = point

    else:
        if point < minpt:
            minpt = point
            amazing += 1
        
        elif point > maxpt:
            maxpt = point
            amazing += 1

print(amazing)