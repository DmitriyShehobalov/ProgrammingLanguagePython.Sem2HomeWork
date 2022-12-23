# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k),
# не превосходящие числа N.
# 5
# 1 2 4
# 17
# 1 2 4 8 16
print("Enter number")
n = int(input())
count = 0
while count <= n:
    if count*2 > n:
        break
    if count == 0:
        count = 1
    else:
        count = count*2
    print(count)
