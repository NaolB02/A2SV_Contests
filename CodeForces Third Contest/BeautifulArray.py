n = int(input())
nums = list(map(int, input().split()))
nums.sort()
negatives = []
zeros = []
positives = []

for num in nums:
    if num < 0:
        negatives.append(num)
    
    elif num > 0:
        positives.append(num)
    
    else:
        zeros.append(num)

if len(positives) == 0:
    positives.append(negatives.pop())
    positives.append(negatives.pop())

if len(negatives) % 2 == 0:
    zeros.append(negatives.pop())

print(len(negatives), end=" ")
for num in negatives:
    print(num, end=" ")

print()

print(len(positives), end=" ")
for num in positives:
    print(num, end=" ")

print()

print(len(zeros), end=" ")
for num in zeros:
    print(num, end=" ")
