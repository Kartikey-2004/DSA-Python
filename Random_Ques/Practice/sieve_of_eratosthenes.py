def sieve(n):
    if n <= 1:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    primes = []

    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


n = int(input("Enter the number : "))
print(sieve(n))
