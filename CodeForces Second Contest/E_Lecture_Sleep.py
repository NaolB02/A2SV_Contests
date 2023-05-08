n, k = map(int, input().split())
theorems = list(map(int, input().split()))
state = list(map(int, input().split()))
summ = max_sum = 0

for i in range(n):
    if state[i]:
        summ += theorems[i]

max_sum = summ
l = 0

for r in range(n):
    if not state[r]:
        summ += theorems[r]
    
    max_sum = max(summ, max_sum)

    if r - l + 1 == k:
        if not state[l]:
            summ -= theorems[l]
        
        l += 1

print(max_sum)