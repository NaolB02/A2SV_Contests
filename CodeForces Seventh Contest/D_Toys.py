from collections import Counter

s, a = map(int, input().split())
Tsemere = list(map(int, input().split()))
Tsemere.sort()

Tandy = []
for _ in range(a):
    Tandy.append(input())

andyDict = Counter(Tandy)
Tandy = []
for toy in andyDict:
    Tandy.append([toy, andyDict[toy]])


Tandy.sort(reverse = True, key=lambda x: x[1])

minPrice = 0
maxPrice = 0
index = 0

for toy in Tandy:
    curPrice = toy[1] * Tsemere[index]
    minPrice += curPrice
    index += 1

index = s - 1
for toy in Tandy:
    curPrice = toy[1] * Tsemere[index]
    maxPrice += curPrice
    index -= 1


print(minPrice, maxPrice)