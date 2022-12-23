# Задача 10
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random
print('Enter the number of coins')
n = int(input())
m = []
count = 0
for i in range(n):
    random_number = random.randint(0, 1)
    m.append(random_number)
    if m[i] == 1:
        count += 1
    if count == n/2:
        print('Need to flip 5 coins')    
print(f'{n} -> {m}')
print(count if count < n/2 else n-count)
