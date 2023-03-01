n = int(input())
members = list(input().split())
badMembers = set(list(input().split()))
count = 0

for member in members:
    if member in badMembers:
        continue
    letterSet = set(list(member))
    if len(letterSet) == len(member):
        count += 1

print(count)
