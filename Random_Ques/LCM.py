def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


# a*b=lcm(a,b)*gcd(a,b)
def lcm(a, b):
    return a * b // GCD(a, b)


if __name__ == "__main__":
    a = 3
    b = 9
    print(lcm(a, b))
