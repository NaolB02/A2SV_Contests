import sys
from collections import defaultdict

sys.setrecursionlimit(2500)

n = int(input())
graph = defaultdict(list)
bosses = []

for i in range(n):
    boss = int(input())
    graph[i + 1]
    
    if boss != -1:
        graph[boss].append(i + 1)
    
    else:
        bosses.append(i + 1)

max_dep = [1]

def dfs(node, dep):
    if dep > max_dep[0]:
        max_dep[0] = dep
    
    if node not in graph:
        return

    for emp in graph[node]:
        dep += 1
        dfs(emp, dep)
        dep -= 1

for node in bosses:
    dfs(node, 1)

print(max_dep[0])