num = int(input())
ans = 0

while num > 1:
    ans += num % 2
    num //= 2

ans += 1
print(ans)