#time complexity is O(n)
n = int(input())

for i in range(n):
    data = input().split("#")
    data = ' '.join(data)
    print(data)