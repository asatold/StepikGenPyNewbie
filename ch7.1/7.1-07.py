"""На вход программе подается натуральное число n (n≥2) - катет прямоугольного равнобедренного треугольника.

Напишите программу, которая выводит звездный треугольник в соответствии c примером.

Формат входных данных
На вход программе подается одно натуральное число n (n≥2)."""

kat = int(input())  # катет треугольника

# def trianglestar(katet: int):
#     for i in range(katet, 0, -1):
#         print(f'*' * i)

def trianglestar(katet):
    for i in range(katet):
        if i < katet:
            print(f'*' * (katet - i))

trianglestar(kat)
