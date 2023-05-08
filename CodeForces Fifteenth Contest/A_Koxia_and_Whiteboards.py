import heapq

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    heap_a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.reverse()
    heapq.heapify(heap_a)


    for i in range(m):
        heapq.heappop(heap_a)
        bi = b.pop()
        heapq.heappush(heap_a, bi)

    print(sum(heap_a))