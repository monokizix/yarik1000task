a = float(input())
n = int(input())

power = 1.0
for i in range(1, n + 1):
    power *= a
    print(power)