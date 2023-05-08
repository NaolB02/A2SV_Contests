n, t = map(int, input().split())
portals = list(map(int, input().split()))
i = 1

while i < t:
    i += portals[i - 1]

if i == t:
    print('YES')

else:
    print('NO')