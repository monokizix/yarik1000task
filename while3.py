n = int(input("input n"))
k = int(input("input k"))
count=0 #счетчик частного 
while n >= k:
    n = n - k
    count += 1
    print("Частное:", count) # вывод после цикла
    print ("остаток:, n")