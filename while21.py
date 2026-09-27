N = int(input("Введите N: "))
has_odd = False  

temp = N
while temp > 0:
    digit = temp % 10      
    if digit % 2 != 0:     
        has_odd = True
        break              
    temp //= 10    

print(has_odd)