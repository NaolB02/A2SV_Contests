n = int(input())

for _ in range(n):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    isPresent = False

    wholesum = sum(nums)
    prefixSum = [wholesum - x for x in nums]
    prefixSum = set(prefixSum)

    for num in nums:
        if (num - k) in prefixSum:
            isPresent = True
    
    if isPresent:
        print("YES")
    
    else:
        print("NO")