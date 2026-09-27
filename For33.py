n = int(input())

f1 = 1
f2 = 1

for i in range(1, n + 1):
    if i == 1:
        print(f1)
    elif i == 2:
        print(f2)
    else:
        f_new = f1 + f2
        f1 = f2
        f2 = f_new
        print(f2)