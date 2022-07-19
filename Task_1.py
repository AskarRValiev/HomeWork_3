#1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random

def odd_position(numbers: list):
    sum = 0
    lst = numbers[1::2]
    for i in lst:
        sum +=i
    return sum


def create_rnd_list():
    rnd_list = []
    for i in range(10):
        rnd_list.append(random.randint(0, 6))
    print(rnd_list)
    return rnd_list


num_list = create_rnd_list()
print(odd_position(num_list))

