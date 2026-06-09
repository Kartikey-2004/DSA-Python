def factorial(n):
    val = 1
    for i in range(1, n + 1):
        val = val * i
    return val


if __name__ == "__main__":
    number = 4
    print(factorial(number))

