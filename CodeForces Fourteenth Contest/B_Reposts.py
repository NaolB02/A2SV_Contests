from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
graph = defaultdict(list)

for _ in range(n):
    edge = list(stdin.readline().split())
    src, dest = edge[2].lower(), edge[0].lower()
    graph[src].append(dest)

start = 'polycarp'
max_depth = 0
visited = set()

def dfs(node, depth):
    global max_depth

    max_depth = max(depth, max_depth)
    visited.add(node)

    for neigh in graph[node]:
        if neigh not in visited:
            dfs(neigh, depth + 1)
    
    return

dfs(start, 1)
print(max_depth)
