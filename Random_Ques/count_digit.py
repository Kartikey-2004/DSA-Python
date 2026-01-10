n = int(input("Enter the number :"))
len = 0
while n > 0:
    n = n // 10
    len += 1

print(f"{len}")
