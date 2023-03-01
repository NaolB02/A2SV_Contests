n, m = map(int, input().split())
remain = list(map(int, input().split()))
costs = list(map(int, input().split()))
custOrd = []

for _ in range(m):
    curOrd = list(map(int, input().split()))
    custOrd.append(curOrd)

costInd = []
for index in range(n):
    costInd.append([])

