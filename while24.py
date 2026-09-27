N = int(input("Введите N: "))

f1, f2 = 1, 1
is_fib = False

if N == 1:
    is_fib = True
else:
    while f2 < N:
        f1, f2 = f2, f1 + f2     
    if f2 == N:
        is_fib = True

print(is_fib)