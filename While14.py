a = float(input("Введите A (>1): "))
s = 0.0
k = 0

while s + 1 / (k + 1) < a:
    k += 1     
    s += 1 / k 

print(k, s)