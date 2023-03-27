t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    start_seconds = list(map(int, input().split()))

    low, high = 0, h

    while low <= high:
        mid = (high + low) // 2
        k = mid
        cur_damage = 0

        for i in range(1, n):
            diff = start_seconds[i] - start_seconds[i - 1]
            cur_damage += min(k, diff)
        cur_damage += k

        if cur_damage >= h:
            high = mid - 1
        
        else:
            low = mid + 1
        
    print(low)