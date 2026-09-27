number = int(input("Введите трехзначное число: "))
c = number % 10
number = number // 10
b = number % 10
a = number // 10
result = a * 100 + c * 10 + b
print(result)