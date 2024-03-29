"""На вход программе подается натуральное число N.
Напишите программу, которая печатает звездный прямоугольник размерами Nx19.
Формат входных данных
На вход программе подаётся натуральное число N ∈ [1; 20] — высота звездного прямоугольника.
Формат выходных данных
Программа должна вывести звездный прямоугольник размерами Nx19."""


count = int(input())  # количество строк прямоугольника
starcount: int = 19  # количество звездочек в строке

def rectanglestar(xcount: int, ycount: int):
    # печатает прямоугольник из starcount звездочек в строке
    mystr: str = '*' * ycount  # строка образующая прямоугольник
    for _ in range(1, xcount + 1):
        print(f'{mystr}')

rectanglestar(count, starcount)
