n = int(input("input n: "))
s = float (0)
o = n
for i in range(1, n+1):
    s = s + i**o
    o = o - 1
print(s)