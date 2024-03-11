"""Даны два целых числа m и n (m > n). Напишите программу, которая выводит все нечетные целые числа от m до n включительно в порядке убывания.
Формат входных данных:
На вход программе подаются два целых числа m и n, каждое на отдельной строке.
Формат выходных данных:
Программа должна вывести числа в соответствии с условием задачи.
Примечание. Попробуйте решить задачу двумя способами: с использованием условного оператора if и без него."""

m, n = int(input()), int(input())

#  функция выводит все нечентые в указанном ряду с использованием условия 
# def printneg(mm: int, nn: int):
#     for i in range(mm, nn - 1, -1):
#         if i % 2 != 0:
#             print(f'{i}')

#  функция выводит все нечентые в указанном ряду без использования условия
def printneg(mm: int, nn: int):
    for i in range((mm % 2 + (mm - 1)), nn - 1, -2):
        print(f'{i}')


printneg(m, n)