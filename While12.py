n = int(input("Введите N: "))
s = 0
k = 0

while s + (k + 1) <= n:
    k += 1
    s += k

print(k, s)