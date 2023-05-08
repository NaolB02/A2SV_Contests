from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    i = 0

    num = nums[0]
    for cur in nums:
        num &= cur
    
    print(num)