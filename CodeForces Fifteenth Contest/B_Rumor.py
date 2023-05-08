from collections import defaultdict


n, m = map(int, input().split())
gold = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a]. append(b)
    graph[b]. append(a)

def dfs

summ = sum(gold)
friends = set()

for a, b in pairs:
