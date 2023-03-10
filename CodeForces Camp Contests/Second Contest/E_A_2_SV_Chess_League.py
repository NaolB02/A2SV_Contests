n, k = map(int, input().split())
players = list(map(int, input().split()))

def get_winners(players, winners = []):
    if len(players) == 2:
        if players[0] > players[1] + k:
            return players[0]
        
        elif players[1] > players[0] + k:
            return players[1]
        
        else:
            return min(players)
    
    else:
        mid = len(players) // 2
        block1 = get_winners(pl)