n = int(input())

a1 = 1.0
a2 = 2.0

for i in range(1, n + 1):
    if i == 1:
        print(a1)
    elif i == 2:
        print(a2)
    else:
        a_new = (a1 + 2 * a2) / 3
        a1 = a2
        a2 = a_new
        print(a2)