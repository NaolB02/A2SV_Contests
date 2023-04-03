t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    for i, num in enumerate(nums):
        x = 0
        for j in range(n):
            if i == j:
                continue
            x ^= nums[j]
        
        if x == num:
            ans = x
    
    print(ans)