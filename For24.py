x = float(input())
n = int(input())

summa = 1.0
term = 1.0

for i in range(1, n + 1):
    # Умножаем на -x*x и делим на (2i-1)*(2i)
    term *= -x * x / ((2 * i - 1) * (2 * i))
    summa += term

print(summa)