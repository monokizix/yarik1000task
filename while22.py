N = int(input("Введите N (>1): "))
is_prime = True
d = 2

while d * d <= N:
    if N % d == 0:
        is_prime = False
        break
    d += 1

print(is_prime)