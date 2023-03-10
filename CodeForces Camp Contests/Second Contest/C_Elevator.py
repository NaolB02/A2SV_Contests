import math

def findBestWay(walk, elev, elev_level, dest = 0, time = 0):
    if dest == 4:
        return time
    
    else:
        walking = findBestWay(walk, elev, elev_level, dest + 1, time + walk)
        
        if dest == elev_level:
            elevating = findBestWay(walk, elev, elev_level + 1, dest + 1, time + elev)
        
        elif dest < elev_level:
            elevating = findBestWay(walk, elev, elev_level - 1, dest, time + elev)
        
        else:
            elevating = math.inf
        
        return min(walking, elevating)
    

t = int(input())

for _ in range(t):
    walk, elev, level = list(map(int, input().split()))

    print(findBestWay(walk, elev, level))
