n = int(input())

for i in range(n):
    size, curlight = input().split()
    size = int(size)
    lights = input()
    stack = []
    time = 0

    for index in range(2 * size):
        light = lights[index % size]

        if light == curlight:
            stack.append(index)
        
        elif stack and light == "g":
            while stack:
                sIndex = stack.pop()
        
            time = max(index - sIndex, time)
    
    print(time)