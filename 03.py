# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint


def gen_int_rnd_list(count):
    int_rnd_list = []

    for _ in range(count):
        int_rnd_list.append(randint(-100, 100))

    return int_rnd_list


def shuffle_list(user_list):
    list_shuffle = []
    index_list = []
    count = 0

    while count != len(user_list):
        index = randint(0, len(user_list) - 1)

        if index in index_list:
            continue
        else:
            old_num = user_list[index]
            list_shuffle.append(old_num)
            index_list.append(index)
            count += 1

    return list_shuffle


count_num = 5                                          # количество элементов списка для теста
rnd_list = gen_int_rnd_list(count_num)
shuffle_rnd_list = shuffle_list(rnd_list)              # для наглядности, вообще по заданию конкретно изначальный список перемешать, но решил так лучше

print(rnd_list)
print(shuffle_rnd_list)