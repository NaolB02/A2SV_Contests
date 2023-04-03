import math
from collections import deque

n, k = map(int, input().split())
ans = deque()

if k > n:
    print('NO')
    exit()

bits = []
i = 0
ano_n = n

while n > 0:
    cur_n = n
    cur_n &= 1

    if cur_n:
        bits.append(2 ** i)

    i += 1
    n >>= 1

if len(bits) > k:
    print('NO')
    exit()

right = []
total = len(right) + len(bits)
while total != k:
    large = bits.pop()
    cur_k = k - len(bits)
    large //= 2
    if large == 1:
        right.append(large)
        right.append(large)
    
    else:
        bits.append(large)
        bits.append(large)
    
    total = len(right) + len(bits)

print('YES')
print(*sorted(bits + right))
