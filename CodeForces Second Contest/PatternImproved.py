from random import randint
from string import ascii_lowercase

n = int(input())
patterns = []
ans = []

for _ in range(n):
    pattern = input()
    patterns.append(pattern)

answer = ''
for col in range(len(patterns[0])):
    answer = patterns[0][col]
    isBroken = False

    for row in range(1, len(patterns)):
        cur = patterns[row][col]

        if answer == '?':
            answer = cur
        
        elif cur != '?' and answer != cur:
            isBroken = True
            answer = '?'
            break
    
    if not isBroken and answer == '?':
        answer = 'n'
    ans.append(answer)

print(''.join(ans))