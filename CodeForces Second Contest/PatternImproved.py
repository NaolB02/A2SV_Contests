from random import randint
from string import ascii_lowercase

n = int(input())
patterns = []

for _ in range(n):
    pattern = input()
    patterns.append(patterns)

answer = ''
for col in range(len(pattern[0])):
    answer = patterns[0][col]
    for row in range(1, len(patterns)):
        if 