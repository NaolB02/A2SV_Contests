size = int(input())
nums = list(map(int, input().split()))
nums.sort()

teams = []
left = 0

if size == 1:
    print(1)

for right in range(1, size):
    if nums[right] > nums[left] + 5:
        teams.append(nums[left:right])
        
        if right == size - 1:
            teams.append([nums[right]])
        
        left = right
    
    elif right == size - 1:
        teams.append(nums[left: right + 1])


maxSum = 0
maxIndex = 0

for index in range(len(teams)):
    if sum(teams[index]) > maxSum:
        maxSum = sum(teams[index])
        maxIndex = index
    
    elif sum(teams[index]) == maxSum and len(teams[index]) > len(teams[maxIndex]):
        maxIndex = index

if teams:
    print(len(teams[maxIndex]))