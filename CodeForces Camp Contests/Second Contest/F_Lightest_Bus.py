def getLightest(weights, first = True):
    if len(weights) < 12:
        return sum(weights)
    
    # elif 12 <= len(weights) < 18:
    elif first:
        b_18 = getLightest(weights, False)
        b_12 = getLightest(weights, False)
    
    else:
        b_18 = getLightest(weights, False)
        b_12 = getLightest(weights, False)



t = int(input())

for _ in range(len(t)):
    n = int(input())
    weights = list(map(int, input().split()))

