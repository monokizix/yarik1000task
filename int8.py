number = int(input("Введите двузначное число: "))
tens = number // 10      
units = number % 10
sum_digits = tens + units
prod_digits = tens * units
print(sum_digits)
print(prod_digits)