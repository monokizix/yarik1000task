n = int(input("введите n "))
S = 0
sign = 1
for i in range(1, n+1):
   M = (1 + i/10)*sign
   S=S+M
   sign = sign * (-1)
print (S)
