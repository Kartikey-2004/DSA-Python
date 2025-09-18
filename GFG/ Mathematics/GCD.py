def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


if __name__ == "__main__":
    a = 3
    b = 5
    print(GCD(a, b))
