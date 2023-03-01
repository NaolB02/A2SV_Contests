num = int(input())
laptops = []
alexState = False

for index in range(num):
    laptop = list(map(int, input().split()))
    laptops.append(laptop)

laptops.sort(key= lambda laptop : laptop[0])

for index in range(num - 1):
    laptop1 = laptops[index]
    laptop2 = laptops[index + 1]
    price1, qual1 = laptop1[0], laptop1[1]
    price2, qual2 = laptop2[0], laptop2[1]

    if qual1 > qual2:
        print("Happy Alex")
        alexState = True
        break
    
if not alexState:
    print("Poor Alex")