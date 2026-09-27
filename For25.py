x = float(input())
n = int(input())

summa = 0.0
term = x

for i in range(1, n + 1):
    if i > 1:
        term *= -x * (i - 1) / i
    summa += term

print(summa)