n = int(input())
sq = int(n ** 0.5)

if n == 1:
    print(1, 1)
    exit()

if sq == n ** 0.5:
    sq -= 1

while sq > 0 and n % sq != 0:
    sq -= 1

di = n // sq
print(sq, di)
