p = float(input("Введите процент увеличения P (0 < P < 50): "))

current_run = 10.0      
total_sum = 10.0        
days = 1                

while total_sum <= 200:
    days += 1
    current_run = current_run * (1 + p / 100)
    total_sum += current_run

print("Дней:", days)
print("Суммарный пробег:", total_sum) 