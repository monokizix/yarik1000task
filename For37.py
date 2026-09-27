n = int(input("input n: "))
s = float(0)
for i in range(1, n+1):
    s = s + i**i    
print(s)