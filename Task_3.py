#3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

def to_fractional(n: float):
    res = n - int(n)
    return res


def large_of_fractional(real_list: list):
    fractional_list = []
    for item in real_list:
        fractional_list.append(to_fractional(item))
    fractional_list.sort()
    result = fractional_list[-1] - fractional_list[0]
    return result


real_list = [1.1, 1.2, 3.1, 5.561, 10.01]
print(large_of_fractional(real_list))