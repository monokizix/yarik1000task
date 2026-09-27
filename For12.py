n = int(input("введите n "))
P = 1

for i in range(1, n+1):
    P = P * (1 + i/10)
print (P)
