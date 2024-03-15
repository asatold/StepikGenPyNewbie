"""На вход программе подается натуральное число n, а затем n различных натуральных чисел последовательности,
каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
Формат входных данных
На вход программе подаются натуральное число n ≥ 2, а затем n различных натуральных чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести два наибольших числа, каждое на отдельной строке."""

n = int(input())


def maxAndSecondmax(nn: int) -> str:
    max: int = 0
    secondmax: int = 0
    for i in range(n):
        dig =  int(input())
        if dig > max:
            max, secondmax = dig, max
        else:
            if dig > secondmax:
                secondmax = dig
    print(f'\n{max}\n{secondmax}')

maxAndSecondmax(n)
