def trial_division_simple(n: int) -> list[int]:
    factorization: list[int] = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d
        d += 1
    if n > 1:
        factorization.append(n)

    return factorization


print(trial_division_simple(6))
