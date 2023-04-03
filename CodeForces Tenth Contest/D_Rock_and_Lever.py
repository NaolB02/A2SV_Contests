from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    sig_bit = [0] * n
    for i, num in enumerate(nums):
        cur = 0
        j = 0

        while num > 0:
            cur_num = num
            cur_num &= 1

            if cur_num:
                cur = max(cur, j)
            
            j += 1
            num >>= 1
        
        sig_bit[i] = cur
    
    sig_bit = Counter(sig_bit)
    ans = 0
    for bit in sig_bit:
        count = sig_bit[bit] - 1
        count = count * (count + 1) // 2        
        ans += count
    
    print(ans)