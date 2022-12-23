# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
print('Enter the sum of the numbers')
a_sum = int(input())
print('Enter the multiplication of the numbers')
a_multiple = int(input())
num1 = 0
while num1 <= a_sum:
    num2 = a_sum - num1
    if num1 * num2 == a_multiple:
        break
    else: num1 += 1

print(f'Первое число -> {num1}, второе число -> {num2}')

