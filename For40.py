a = int(input("input: a "))
b = int(input("input: b "))
n = 1
for i in range (a, b+1):
    for j in range(1, n+1):
     print(i, end =" ")
    n = n+1
    print()