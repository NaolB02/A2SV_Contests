t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))

    summ = (x * (x + 1)) // 2

    for num in nums:
        if num <= x:
            summ -= 2 * num
    
    print(summ)