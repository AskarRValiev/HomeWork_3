#4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def decimal_to_binary(n: int):
    binary = []

    while n > 0:
        if n % 2 == 0:
            binary.insert(0,0)
        else:
            binary.insert(0,1)
        n //= 2
    return binary



n = input('Enter positive integer: ')
if n.isdigit() == False:
    print('It\'s not positive integer!')
    exit()
else:
    print('From decimal {} to binary is {}'.format(n, decimal_to_binary(int(n))))
