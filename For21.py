n = int(input())

summa = 1.0
factorial = 1.0
for i in range(1, n + 1):
    factorial *= i
    summa += 1 / factorial
print(summa)