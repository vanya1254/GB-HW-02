# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num = float(input("Enter number --> "))
# sum = 0

# while round(num, 10) != int(num):              # работает для положительных и отрицательных до 10 знаков после запятой
#     num *= 10

# int_abs_num = abs(int(num))

# while int_abs_num != 0:
#     sum += int_abs_num % 10
#     int_abs_num //= 10

# print(sum)


num = abs(float(input("Enter number --> ")))
split_num = str(num).split('.')                  # вроде для всех чисел до 14 знаков после запятой
sum = 0

# for i in split_num:
#     for j in split_num[i]:                     # понял ошибку, но не понял почему не работает, ниже сделал по-другому немного
#         sum += int(j)

for i in split_num[0]:
    sum += int(i)
for j in split_num[1]:
    sum += int(j)

print(sum)