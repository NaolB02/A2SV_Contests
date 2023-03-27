from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
slidin_win = defaultdict(int)
ans = []

for right in range(n):
    if right == 0:
        pass
    
    elif abs(nums[right] - nums[right - 1]) != 1:
        while slidin_win:
            slidin_win[nums[left]] -= 1
            
            if slidin_win[nums[left]] == 0:
                del slidin_win[nums[left]]
            
            left += 1

    slidin_win[nums[right]] += 1

    while len(slidin_win) > k:
        
        slidin_win[nums[left]] -= 1

        if slidin_win[nums[left]] == 0:
            del slidin_win[nums[left]]
        
        left += 1
    
    ans.append([left + 1, right + 1])

out = max(ans, key= lambda x: x[1] - x[0] + 1)
print(out[0], out[1])
