from collections import deque

size = int(input())
nums = list(map(int, input().split()))
circleable = True
nums.sort()
numsDeque = deque()

numsDeque.append(nums.pop())
while len(nums) > 1:
    numsDeque.append(nums.pop())
    numsDeque.appendleft(nums.pop())

if len(nums) == 1:
    numsDeque.append(nums[-1])

nums = list(numsDeque)

for index in range(len(nums)):
    if index == 0:
        if nums[0] >= nums[1] + nums[size - 1]:
            circleable = False
            print("NO")
            break
    
    elif index == size - 1:
        if nums[size - 1] >= nums[0] + nums[size - 2]:
            circleable = False
            print("NO")
            break
    
    else:
        if nums[index] >= nums[index - 1] + nums[index + 1]:
            circleable = False
            print("NO")
            break

if circleable:
    print("YES")
    nums = list(map(str, nums))
    print(" ".join(nums))