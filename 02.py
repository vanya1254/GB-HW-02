# Задайте список из n чисел последовательности (1 + 1/n)^n, 
# выведеите его на экран, 
# а так же сумму элементов списка.
# 
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


n = int(input("Enter length sequence --> "))
# sequence = get_sequence(n)

n_list = []
sum = 0

for i in range((abs(n) // n), (n + (abs(n) // n)),  (abs(n) // n)):         # не знаю зачем, но сделал и для отрицательных от -1 до -4 при n = -4
    if i == -1:                                                             # -1 пропускаю из-за ошибки по формуле
        continue
    n_list.append(round((1 + 1/i)**i, 2))
print(f"Для n = {n} -> {n_list}")

for i in n_list:
    sum += i
print(f"Amount of sequence == {sum}")



# def get_sequence(num):
#     num_list = []
    
#     for i in range(1, num + 1):
#         num_list.append(round((1 + 1/i)**i, 2))
        
#     print(f"Для n = {num} -> {num_list}")
    
#     get_sum_list(num_list)                                                # только для положительных/ запихнул в функции с вызовом другой прямо из функции, потестить хотел

# def get_sum_list(num_list):
#     sum = 0
    
#     for i in num_list:
#         sum += i
        
#     print(f"Amount of sequence == {sum}")