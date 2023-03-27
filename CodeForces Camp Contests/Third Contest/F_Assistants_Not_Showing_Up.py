n, m = map(int, input().split())
ranges = []

for _ in range(m):
    range_ = list(map(int, input().split()))
    ranges.append(range_)

days = [0] * n

for start, end in ranges:
    days[start] += 1
    
    if end != n - 1:
        days[end + 1] -= 1

for i in range(1, n):
    days[i] += days[i - 1]
try:
    prescence = days.index(0)
    print("YES")

except:
    print("NO")