t = int(input())

for _ in range(t):
    recs = int(input())
    sides = list(map(int, input().split()))
    sides.sort()
    
    
    isValid = True
    left, right = 0, len(sides) - 1
    area = sides[left] * sides[right]
    cur_recs = 0

    while left < right:
        cur_area = sides[left] * sides[right]

        if cur_area != area:
            print("NO")
            isValid = False
            break
            
        if left % 2 != 0 and right % 2 == 0:
            if sides[left] != sides[left - 1] or sides[right] != sides[right + 1]:
               print("NO")
               isValid = False
               break 

            else:
                cur_recs += 1

        left += 1
        right -= 1

    if isValid and cur_recs != recs:
        print("NO")
        isValid = False
    
    if isValid:
        print("YES")
