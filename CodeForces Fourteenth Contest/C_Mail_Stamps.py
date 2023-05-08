from sys import stdin
from collections import defaultdict
from collections import deque

n = int(stdin.readline())
graph = defaultdict(list)

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

src = None
dest = None
for node in graph:
    if not src and len(graph[node]) == 1:
        src = node

    elif src and len(graph[node]) == 1:
        dest = node
        break

path = {src: None}
queue = deque([src])

while queue:
    node = queue.popleft()

    if node == dest:
        goal = node
        break

    for neigh in graph[node]:
        if neigh not in path:
            path[neigh] = node
            queue.append(neigh)

final_path = []
while goal:
    final_path.append(goal)
    goal = path[goal]

print(*final_path)