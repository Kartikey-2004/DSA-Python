def divisor(n):
    divisors = []
    i = 1
    while i * i < n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    if i * i == n:
        divisors.append(i)
        i -= 1
    while i >= 1:
        if n % i == 0:
            divisors.append(n // i)
        i -= 1
    return sorted(divisors)


n = int(input("Enter the number : "))
print(divisor(n))
