size = int(input())
nums = list(map(int, input().split()))

edward = 0
alphonse = 0

start = 0
end = size - 1

while start < end:
    if start == end - 1:
         edward += 1
         alphonse += 1
         break
    
    elif nums[start] > nums[end]:
        nums[start] -= nums[end]
        end -= 1
        alphonse += 1
    
    elif nums[start] < nums[end]:
        nums[end] -= nums[start]
        start += 1
        edward += 1
    
    elif nums[start] == nums[end]:
        start += 1
        end -= 1
        edward += 1
        alphonse += 1

if start == end:
        edward += 1

print(edward, alphonse)
