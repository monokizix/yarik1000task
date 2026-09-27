number = int(input("Введите трехзначное число: "))
c = number % 10
number = number // 10 
b = number % 10
a = number // 10
summ = a + b + c
equals = a * b * c
print(summ)
print(equals)