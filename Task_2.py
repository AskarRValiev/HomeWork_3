#2 - Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

def create_rnd_list():
    '''
    Creat list of 10 random integer from 1 to 10

    '''
    rnd_list = []
    for i in range(10):
        rnd_list.append(random.randint(1, 10))
    print(rnd_list)
    return rnd_list


def couple_sum(numbers: list):
    '''
    Create new list from recieved list.

    New list obtained by multiplying couples of recieved list.
    '''
    result_list = []
    if len(numbers) % 2 == 0:
        for i in range(len(numbers)//2):
            result_list.append(numbers[i] * numbers[len(numbers)-1-i])
    else:
        for i in range(len(numbers)//2+1):
            result_list.append(numbers[i] * numbers[len(numbers)-1-i])
    return result_list


print(couple_sum(create_rnd_list()))
