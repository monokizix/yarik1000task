xa = float(input("Введите координату A: "))
xb = float(input("Введите координату B: "))
xc = float(input("Введите координату C: "))
ac = abs(xc - xa)
bc = abs(xc - xb)
sum_segments = ac + bc
print(ac)
print(bc)
print(sum_segments)