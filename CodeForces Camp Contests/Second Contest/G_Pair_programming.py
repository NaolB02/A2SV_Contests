n, k = map(int, input().split())
durations = list(map(int, input().split()))
durations.sort()
low, high = 0, len(durations) - 1
total_time = 0

while k > 0:
    mid = low + (high - low) // 2
    session = min(k, mid - low + 1)

    total_time += (session * durations[mid])
    k -= session
    low = mid + 1

print(total_time)