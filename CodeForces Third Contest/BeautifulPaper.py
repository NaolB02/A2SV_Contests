n = int(input())

for _ in range(n):
    firstRec = list(map(int, input().split()))
    secondRec = list(map(int, input().split()))

    for _ in range(1):
        if firstRec[0] == secondRec[0]:
            curSum = firstRec[1] + secondRec[1]
            
            if curSum == firstRec[0]:
                print("Yes")
                break
        
        if firstRec[0] == secondRec[1]:
            curSum = firstRec[1] + secondRec[0]
            
            if curSum == firstRec[0]:
                print("Yes")
                break
        
        if firstRec[1] == secondRec[0]:
            curSum = firstRec[0] + secondRec[1]
            
            if curSum == firstRec[1]:
                print("Yes")
                break
        
        if firstRec[1] == secondRec[1]:
            curSum = firstRec[0] + secondRec[0]
            
            if curSum == firstRec[1]:
                print("Yes")
                break
        
        print("No")