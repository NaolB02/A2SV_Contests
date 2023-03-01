size = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
nums[0], nums[1] = nums[1], nums[0]

if nums[0] + nums[2] > nums[1]:
    print("YES")
    print(" ".join(map(str, nums)))

else:
    print("NO")