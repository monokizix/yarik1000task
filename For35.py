n = int(input("input n: "))

a1 = 1
a2 = 2
a3 = 3

print(a1)
print(a2)
print(a3)

for k in range(4, n + 1):
    ak = a3 + a2 - 2 * a1

    print(ak)

    a1 = a2
    a2 = a3
    a3 = ak