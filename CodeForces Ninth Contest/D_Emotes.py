n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

quo = m // (k + 1)
rem = m % (k + 1)

large = nums[-1]
small = nums[-2]

happiness = (quo * ((k * large) + small)) + (rem * large)
print(happiness)
