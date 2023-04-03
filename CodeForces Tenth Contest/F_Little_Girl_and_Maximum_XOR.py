l, r = map(int, input().split())
xor = l ^ r

count = 0
cur_xor = xor
while cur_xor > 0:
    count += 1
    cur_xor >>= 1

if count > 0:
    all_one = 2 ** count - 1
    print(all_one | xor)

else:
    print(xor)