n, k, q = map(int, input().split())
recipes = []
questions = []

for _ in range(n):
    newr = list(map(int, input().split()))
    recipes.append(newr)

for _ in range(q):
    newq = list(map(int, input().split()))
    questions.append(newq)

maxTemp = max(recipes, key=lambda x: x[1])[1]
maxq = max(questions, key=lambda x: x[1])[1]
maxTemp = max(maxTemp, maxq)

minTemp = min(recipes, key=lambda x: x[0])[0]
minq = min(questions, key=lambda x: x[0])[0]
minTemp = min(minq, minTemp)

temps = [0] * (maxTemp + 2 - minTemp)

for rec in recipes:
    temps[rec[0] - minTemp] += 1
    temps[rec[1] + 1 - minTemp] -= 1

for index in range(1, len(temps)):
    temps[index] += temps[index - 1]

for index in range(len(temps)):
    if temps[index] >= k:
        temps[index] = 1
    
    else:
        temps[index] = 0

for index in range(1, len(temps)):
    temps[index] += temps[index - 1]

for question in questions:
    initial = question[0] - minTemp - 1
    terminal = question[1] - minTemp

    if initial < 0:
        result = temps[terminal]

    else:
        result =  temps[terminal] - temps[initial]

    print(result)