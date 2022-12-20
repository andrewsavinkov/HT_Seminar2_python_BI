# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def input_float():
    number=input('Введите вещественное число: ')
    try:
        number=float(number)
        return number
    except:
        print('Вы ввели некорректное число! Попробуйте снова!')

def digit_sum(float_input):
    str_input=str(float_input)
    only_digits=str_input.split('.')
    new_lst=[]
    for i in range(len(only_digits[0])):
        new_lst.append(int(only_digits[0][i]))
    for i in range(len(only_digits[1])):
        new_lst.append(int(only_digits[1][i]))
    print(new_lst)
    print(f'{float_input} -> {sum(new_lst)}')

input_num = input_float()
digit_sum(input_num)



# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n=4
def create_lst(n):
    lst=[]
    for i in range(1, n+1):
        n=(1+1/i)**i
        n=round(n, 2)
        lst.append(n)
    print(lst)
    print(f'Сумма {sum(lst)}')

create_lst(n)

# 3.    Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ
#       SHUFFLE, максимум использование библиотеки Random для получения случайного int
from random import randint

def shuffle_list(input_list):
    lst=[]
    previous_rands=[]
    rand_num=randint(0, len(input_list)-1)
    for i in range(len(input_list)):
        while rand_num in previous_rands:
            rand_num = randint(0, len(input_list) - 1)
        previous_rands.append(rand_num)
        lst.append(input_list[rand_num])
    print(lst)

some_lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
shuffle_list(some_lst)