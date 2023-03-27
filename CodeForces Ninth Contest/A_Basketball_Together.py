n, enemy = map(int, input().split())
powers = list(map(int, input().split()))
powers.sort()

left, right = 0, n - 1
summ = powers[right]
wins = 0

while right > 0 and summ > enemy:
    wins += 1
    right -= 1
    summ = powers[right]

while left < right:
    summ += powers[right]

    if summ > enemy:
        wins += 1
        left += 1
        right -= 1
        summ = powers[right]
    
    else:
        left += 1

if left == right and summ > enemy:
    wins += 1

print(wins)
