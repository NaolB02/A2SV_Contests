n = int(input())

for _ in range(n):
    size, k = map(int, input().split())
    nums = list(map(int, input().split()))
    left = 0
    count = 0

    for right in range(1, size):
        if nums[right] * 2 <= nums[right - 1]:
            left = right
        
        if right - left == k:
            count += 1
            left += 1
    
    print(count)