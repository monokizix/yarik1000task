n = int(input("input n: "))
k = int(input("input k: "))
s = float(0)
for i in range(1, n+1):
    s = s + i**k
print(s)
