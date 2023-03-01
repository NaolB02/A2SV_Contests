import math
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input()))
    minStack = []
    left = -math.inf
        
    for index, num in enumerate(nums):
        while minStack and num > minStack[-1][0]:
            poppedNum, poppedInd = minStack.pop()
            minDiff = min(poppedInd - left, index - poppedInd)

            if poppedInd - left == index - poppedInd:
                pass
            
            elif minDiff <= m:
                nums[poppedInd] = 1
        
        minStack.append([num, index])
        if num == 1:
            left = index
    
    while minStack:
        poppedNum, poppedInd = minStack.pop()
        minDiff = poppedInd - left
        
        if minDiff <= m:
            nums[poppedInd] = 1

    nums = list(map(str, nums))
    print("".join(nums))