n = int(input("Введите N (>0): "))

found = False

while n > 0 and not found: 
    digit = n % 10
    if digit == 2:
        found = True 
    n = n // 10

if found:
    print("TRUE")
else:
    print("FALSE")