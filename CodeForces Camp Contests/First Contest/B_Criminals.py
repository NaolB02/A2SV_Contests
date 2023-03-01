t = int(input())

for _ in range(t):
    size = int(input())
    nums = list(map(int, input().split()))

    left = 0
    right = 1
    operations = 0
    
    while right < size:
        if nums[left] == 0 and right == left + 1:
            left += 1
            right += 1
        
        elif nums[left] == 0:
            left += 1
        
        elif nums[right] == 0:
            nums[left] -= 1
            nums[right] += 1
            right += 1
            operations += 1
        
        else:
            right += 1
    
    

    for index in range(size - 1):
        operations += nums[index]
    
    print(operations)