import math

n, m, k = map(int, input().split())
players = []

for i in range(m + 1):
    players.append(int(input()))

fedor = players.pop()
count = 0

for player in players:
    diff = 0
    mx = max(player, fedor)
    cpy_fedor = fedor
    rng = int(math.log(mx, 2))

    for _ in range(rng + 1):
        xor = player ^ cpy_fedor

        if xor % 2:
            diff += 1

        player >>= 1
        cpy_fedor >>= 1
    
    if diff <= k:
        count += 1

print(count)