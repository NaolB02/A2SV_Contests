t = int(input())

for _ in range(t):
    students, dividers = map(int, input().split())
    nums = list(map(int, input().split()))
    outlets = 2
    
    if students <= outlets:
        print(0)
    
    else:
        ans = 0
        nums.sort()

        for right in range(dividers - 1, -1, -1):
            outlets += nums[right] - 1
            ans += 1
            
            if students <= outlets:
                break
        
        if students <= outlets:
            print(ans)
        
        else:
            print(-1)