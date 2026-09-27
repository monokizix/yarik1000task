x = float(input())
n = int(input())

summa = 1.0
term = 1.0

for i in range(1, n + 1):
    term *= x * (3 - 2 * i) / (2 * i)
    summa += term

print(summa)