number = int(input("Введите двузначное число: "))
tens = number // 19
units = number % 10
new_number = units * 10 + tens
print(new_number)