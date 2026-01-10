def power(x, n):
    if n == 0:
        return 1
    temp = power(x, n // 2)
    temp = temp * temp
    if n % 2 == 0:
        return temp
    else:
        return temp * x


n = int(input("Enter the number : "))
x = int(input("Enter the number : "))
print(power(n, x))
