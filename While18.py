n = int(input("Введите N (>0): "))

count = 0   
s = 0
    
while n > 0:
    digit = n % 10
    count += 1 
    s += digit  
    n = n // 10 

print("Количество:", count)
print("Сумма:", s)