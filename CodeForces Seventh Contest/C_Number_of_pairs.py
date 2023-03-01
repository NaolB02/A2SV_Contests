n = int(input())
boys = list(map(int, input().split()))
boys.sort()

m = int(input())
girls= list(map(int, input().split()))
girls.sort()

boyPt, girlPt = 0, 0
pairs =  0

while boyPt < n and girlPt < m:
    curBoy = boys[boyPt]
    curGirl = girls[girlPt]

    if curBoy == curGirl or abs(curGirl - curBoy) == 1:
        pairs += 1
        boyPt += 1
        girlPt += 1
    
    elif curBoy < curGirl:
        boyPt += 1
    
    else:
        girlPt += 1

print(pairs)
