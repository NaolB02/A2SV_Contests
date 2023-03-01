size = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

aMinusb = []

for index in range(size):
    aMinusb.append(a[index] - b[index])

