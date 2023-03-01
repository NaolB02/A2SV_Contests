from collections import defaultdict

n = int(input())

for _ in range(n):
    nums = input()
    nums = [int(num) for num in nums]
    numsDict = defaultdict(int)
    left = 0
    minLen = 200001

    for right, num in enumerate(nums):
        numsDict[num] += 1

        while len(numsDict) >= 3:
            minLen = min(minLen, right - left + 1)
            numL = nums[left]
            numsDict[numL] -= 1
            
            if numsDict[numL] == 0:
                del numsDict[numL]
            
            left += 1
    
    if minLen == 200001:
        print(0)
    else:
        print(minLen)
            