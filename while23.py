A = int(input("Введите A: "))
B = int(input("Введите B: "))

while B != 0:
    A, B = B, A % B 

print(f"НОД = {A}")