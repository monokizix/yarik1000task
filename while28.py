e = float(input("Введите epsilon: "))

a = 2.0       
k = 1         
while True:
    new_a = 2 + 1 / a       
    
    if (new_a - a) < e:
        print(k + 1, new_a, a)
        break
        
    a = new_a   
    k += 1      