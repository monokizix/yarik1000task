x = float(input())
n = int(input())

summa = x
term = x

for i in range(1, n + 1):
    # Умножаем на -x*x и делим на (2i)*(2i+1)
    term *= -x * x / ((2 * i) * (2 * i + 1))
    summa += term

print(summa)