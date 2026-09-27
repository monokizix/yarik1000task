p = float(input("Введите процент P (0 < P < 25): "))
s = 1000.0
k = 0

while s <= 1100:
    s = s * (1 + p / 100)
    k += 1 

print(k, s)