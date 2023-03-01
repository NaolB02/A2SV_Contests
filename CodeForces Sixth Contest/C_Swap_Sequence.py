size = int(input())
nums = list(map(int, input().split()))
newNums = sorted(nums)
swaps = []
index1 = 0

for index, newNum in enumerate(newNums):
    num = nums[index1]
    if num == newNum:
       pass

    else:
        right = nums.index(newNum)
        nums[index1], nums[right] = nums[right], nums[index1]
        swaps.append([index1, right])
       
    index1 += 1

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])