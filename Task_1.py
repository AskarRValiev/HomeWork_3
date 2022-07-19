#1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def odd_position(numbers: list):
    sum = 0
    lst = numbers[1::2]
    for i in lst:
        sum +=i
    return sum


num_list = [2, 3, 5, 9, 3, 8]
print(odd_position(num_list))

