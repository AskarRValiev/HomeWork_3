#5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n: int):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def nega_fib(k: int):
    fib_list = [0]
    for i in range(1, k+1):
        n = fib(i)
        fib_list.append(n)
        fib_list.insert(0, ((-1)**(i+1))*n)
    return fib_list

n = input('Enter positive integer: ')
if n.isdigit() == False:
    print('It\'s not positive integer!')
    exit()

print('Fibonacci series is ', nega_fib(int(n)))


