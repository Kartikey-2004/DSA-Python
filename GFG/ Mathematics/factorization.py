def is_prime(s):
    for i in range(2, s):
        if s % i == 0:
            return False
    return True


def factor(n):
    factor = []
    for i in range(2, n + 1):
        if is_prime(i):
            x = i
            while n % i == 0:
                factor.append(i)
                n //= i
    return factor


n = int(input("Enter the number : "))
print(factor(n))
