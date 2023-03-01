n = int(input())

for i in range(n):
    n, curlight = input().split()
    n = int(n)
    lights = input()
    curtime, time = 0, 0

    for i, light in enumerate(lights):
        if light == curlight:
            while lights[i] != 'g':
                curtime += 1

                if i == len(lights) - 1:
                    i = 0

                else:
                    i += 1
                    
            time = max(curtime, time)
            curtime = 0

    print(time)
        