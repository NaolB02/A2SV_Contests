n = int(input())


for _ in range(n):
    curPattern = input()
    if _ == 0:
        pattern = list(curPattern)
        if n == 1:
            for index in range(len(pattern)):
                if pattern[index] == "?":
                    pattern[index] = 'c'
    
    else:
        for index, letter in enumerate(pattern):
            if letter == '?':
                if curPattern[index] == "?":
                    pattern[index] = 'c'

                else:
                    pattern[index] = curPattern[index]
            
            else:
                if curPattern[index] == '?':
                    continue

                elif pattern[index] != curPattern[index]:
                    pattern[index] = '?'

print(''.join(pattern))