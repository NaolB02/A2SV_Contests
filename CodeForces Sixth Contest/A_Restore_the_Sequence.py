t = int(input())

for _ in range(t):
    size = int(input())
    nums = list(map(int, input().split()))
    newNums = [0] * size
    start, end = 0, size - 1
    turn = True

    for index in range(size):
        if turn:
            turn = False
            newNums[index] = nums[start]
            start += 1
        
        else:
            turn = True
            newNums[index] = nums[end]
            end -= 1
    
    print(*newNums)