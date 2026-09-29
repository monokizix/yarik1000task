a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

squares_in_row = 0
temp_a = a
while temp_a >= c:
    temp_a -= c
    squares_in_row += 1

total = 0
temp_b = b
while temp_b >= c:
    total += squares_in_row
    temp_b -= c
print(total)