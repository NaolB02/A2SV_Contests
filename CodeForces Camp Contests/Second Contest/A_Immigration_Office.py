size = int(input())
names = list(input().split())

newCount = int(input())
for _ in range(newCount):
    new_name = input()
    low, high = 0, size - 1

    while low <= high:
        mid = low + (high -  low) // 2

        if names[mid] > new_name:
            high = mid - 1
        
        else:
            low = mid + 1
    
    print(low)