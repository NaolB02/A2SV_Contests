import math

n, a, b = map(int, input().split())
nums = list(map(int, input().split()))
less_than_a = 0
less_than_b = 0

left = 0
summ = 0
for right in range(n):
    summ += nums[right]

    while summ >= a:
      
        summ -= nums[left]
        left += 1
    
    less_than_a += right - left + 1

left = 0
summ = 0
for right in range(n):
    summ += nums[right]

    while summ > b:
      
        summ -= nums[left]
        left += 1
    
    less_than_b += right - left + 1

print(less_than_b - less_than_a)