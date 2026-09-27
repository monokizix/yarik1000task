a = float(input())
n = int(input())

summa = 1.0
power = 1.0
for i in range(1, n + 1):
    power *= -a
    summa += power
print(summa)