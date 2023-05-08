import sys

counts = []
offset = 97
ans = 0

for i, line in enumerate(sys.stdin):
    if i == 0:
        n = int(line.rstrip())
        continue

    cur = line.rstrip()
    count = [0] * 26
    
    for letter in cur:
        count[ord(letter) - offset] += 1
    
    counts.append(count)
    

# n = int(input())
# counts = []
# offset = 97
# ans = 0

# for i in range(n):
#     cur = input()
#     count = [0] * 26
    
#     for letter in cur:
#         count[ord(letter) - offset] += 1
    
#     counts.append(count)

for i in range(n):
    cur = counts[i]

    for j in range(i + 1, n):
        new = counts[j]
        summ = [cur[k] + new[k] for k in range(26)]
        odds = list(filter(lambda x: x % 2 != 0, summ))

        if len(odds) <= 1:
            ans += 1

print(ans)