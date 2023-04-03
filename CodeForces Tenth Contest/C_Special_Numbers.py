t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ans = 0
    i = 0

    while k > 0:
        cur_k = k
        cur_k &= 1

        if cur_k:
            ans += (n ** i)

        i += 1
        k >>= 1

    print(ans % (10 ** 9 + 7))