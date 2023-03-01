size = int(input())
nums = list(map(int, input().split()))
operations = 0
neg = 0
zeros = 0


for index, num in enumerate(nums):
    newNum = num

    if num < 0:
        neg += 1
        newNum += (abs(num) - 1)
        operations += (abs(num) - 1)
        nums[index] = newNum
    
    elif num == 0:
        zeros += 1

    else:
        newNum -= (num - 1)
        operations += (num - 1)
        nums[index] = newNum


if zeros and neg % 2 != 0:
    operations += zeros

elif neg % 2 == 0:
    operations += zeros

else:
    operations += 2

print(operations)
