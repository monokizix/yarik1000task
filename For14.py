n = int(input("Введите N: "))
s = 0

for i in range(1, n + 1):
    num = 2 * i - 1
    s = s + num    
print(s)