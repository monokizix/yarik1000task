x = float(input())
n = int(input())

summa = x
term = x

for i in range(1, n + 1):
    term *= -x * x * (2 * i - 1) / (2 * i + 1)
    summa += term

print(summa)