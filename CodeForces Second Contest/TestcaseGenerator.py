from string import ascii_letters

print(len(ascii_letters))

for i in range(2000):
    ind = i % 52
    print(str(i) + ascii_letters[ind], end = " ")

