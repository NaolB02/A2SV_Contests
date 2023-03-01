# time complexity is O(n^2) because of string concatenation
n = int(input())

for i in range(n):
    data = input()
    individualData = ''

    for letter in data:
        if letter == "#":
            print(individualData, end=' ')
            individualData = ""

        else:
            individualData += letter
    
    print(individualData)