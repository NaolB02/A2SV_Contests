lines = int(input())
code = []

for line in range(lines):
    code.append(input())

stack = [[1, 0]]

for line in code:
    if line == 'add':
        stack[-1][1] += 1
    
    elif line == 'end':
        iteration, num = stack.pop()
        stack[-1][1] += iteration * num
    
    else:
        line = line.split()
        stack.append([int(line[-1]), 0])

if stack[-1][1] >= (2 ** 32):
    print("OVERFLOW!!!")
else:
    print(stack[-1][1])