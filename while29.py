e = float(input("Введите epsilon: "))

a1 = 1.0    
a2 = 2.0    
k = 2  

while True:

    a3 = (a1 + 2 * a2) / 3
    
    if (a3 - a2) < e:
        print(k + 1, a3, a2)
        break

    a1 = a2
    a2 = a3
    k += 1