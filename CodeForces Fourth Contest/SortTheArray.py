size = int(input())
nums = list(map(int, input().split()))

start = 0
end = size - 1

isDone = True

for index in range(size - 1):
    if nums[index] > nums[index + 1]:
        isDone = False

for index in range(size - 1):
    if nums[start] > nums[start + 1]:
        break

    start += 1

for index in range(size - 1):
    if nums[end] < nums[end - 1]:
        break

    end -= 1


nums[start: end + 1] = reversed(nums[start: end + 1])

isSorted = True
for index in range(size - 1):
    if nums[index] > nums[index + 1]:
        isSorted = False
        print("no")
        break

if isSorted and not isDone:
    print("yes")
    if start == size - 1 and end:
        start = 0
    print(start + 1, end + 1)

elif isDone:
    print("yes")
    print(1, 1)