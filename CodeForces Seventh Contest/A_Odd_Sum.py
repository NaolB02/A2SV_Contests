from collections import deque


size = int(input())
array = list(map(int, input().split()))
leftSum, rightSum= sum(array[:size]), sum(array[size:])
array = deque(array)
found = False


for index in range(size):
    equal = (rightSum == leftSum)
    if equal:
        num = array.popleft()
        array.append(num)
        rightSum = rightSum - array[size - 1] + array[-1]   
        leftSum = leftSum + array[size - 1] - array[-1]   

    else:
        found = True
        print(*list(array))
        break

if not found:
    print(-1)