a, b = map(int, input().split())
path = []

def backtrack(fr):
    global b

    if fr == b:
        path.append(fr)
        return True

    elif fr > b:
        return False
    
    # choice 1 -  doubling
    path.append(fr)
    res = backtrack(2 * fr)
    
    if res == True:
        return True
    
    path.pop()

    # choice 2
    path.append(fr)
    res = backtrack(10 * fr + 1)

    if res == True:
        return True
    
    path.pop()

res = backtrack(a)

if res:
    print("YES")
    print(len(path))
    print(*path)

else:
    print("NO")