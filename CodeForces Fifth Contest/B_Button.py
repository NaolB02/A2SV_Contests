n = int(input())

for _ in range(n):
    screen = input()
    letters = set()
    left = 0
    right = 1

    while left < len(screen):
        if right < len(screen) and screen[right] == screen[left]:
            left = right + 1
            right = left + 1
        
        else:
            letters.add(screen[left])
            left += 1
            right += 1
    
    print("".join(sorted(list(letters))))
