import heapq


t = int(input())
for _ in range(t):
    n = int(input())
    soc = list(map(int, input().split()))

    count = 0
    soc = [(-soc[i], i + 1) for i in range(len(soc))]
    heapq.heapify(soc)

    first_max, i = heapq.heappop(soc)
    second_max, j = heapq.heappop(soc)
    meetings = []

    while first_max != 0 and second_max != 0:
        first_max += 1
        second_max += 1
        count += 1
        meetings.append([i, j])

        heapq.heappush(soc, (first_max, i))
        heapq.heappush(soc, (second_max, j))
        
        first_max, i = heapq.heappop(soc)
        second_max, j = heapq.heappop(soc)
    
    print(count)
    for meeting in meetings:
        print(*meeting)
    

    