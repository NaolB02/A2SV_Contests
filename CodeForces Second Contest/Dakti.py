n = int(input())

for _ in range(n):
    song = list(input().split())
    arranged = []
    
    for word in song:
        index = []
        letters = []
        
        for letter in word:
            if letter.isnumeric():
                index.append(letter)

            else:
                letters.append(letter)
        
        letters = ''.join(letters)
        index = ''.join(index)
        arranged.append([letters, index])
    
    arranged.sort(key = lambda x: int(x[1]))
    arrangedChorus = []

    for word, ind in arranged:
        arrangedChorus.append(word)
    
    print(' '.join(arrangedChorus))

