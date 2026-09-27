number = int(input("Введите двузначное число: "))
digit1 = number // 10
digit2 = number % 10
sum_digits = digit1 + digit2
prod_digits = digit1 * digit2
print(sum_digits)
print(prod_digits)