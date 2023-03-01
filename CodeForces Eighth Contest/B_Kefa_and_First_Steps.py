size = int(input())
nums = list(map(int, input().split()))

left = 0
maxLen = 0

if size == 1:
    maxLen = 1

for right in range(1, size):
    if nums[right] < nums[right - 1]:
        maxLen = max(maxLen, right - left)
        left = right
    
    elif right == size - 1:
        maxLen = max(maxLen, right - left + 1)
    

print(maxLen)