size = int(input())

cards = list(map(int, input().split()))
scores = [0,0]
turn = 0

start = 0
end = size - 1

while start <= end:
    if cards[start] > cards[end]:
        scores[turn] += cards[start]
        start += 1
    
    else:
        scores[turn] += cards[end]
        end -= 1
    
    if turn == 1:
        turn = 0
    else:
        turn += 1

print(scores[0], scores[1])