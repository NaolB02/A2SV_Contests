from collections import defaultdict

n = int(input())

primes = defaultdict(int)
primes[2] += 1

colors = [0] * n
colors[0] = 1

for i in range(3, n + 2):
    not_prime = False

    for prime in primes:
        if i % prime == 0:
            not_prime = True
            colors[i - 2] = primes[prime] + 1
            continue
        
    if not_prime:
        continue
    
    primes[i] += 1
    colors[i - 2] = primes[i]

print(len(set(colors)))
print(*colors)