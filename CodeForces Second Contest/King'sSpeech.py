n = int(input())

for _ in range(n):
    word = input()
    repeated = word[:2]
    print(repeated + '... ' + word + '?')