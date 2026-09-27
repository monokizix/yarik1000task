N = int(input("Введите N (число Фибоначчи): "))
f1, f2 = 1, 1

while f2 < N:
    f1, f2 = f2, f1 + f2

prev_fib = f1
next_fib = f1 + f2

print(f"Предыдущее: {prev_fib}, Текущее: {N}, Следующее: {next_fib}")