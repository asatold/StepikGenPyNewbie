"""Даны два целых числа m и n ( m ≤ n). Напишите программу, которая выводит все целые числа от m до n включительно.
Формат входных данных:
На вход программе подаются два целых числа m и n, каждое на отдельной строке."""

m, n = int(input()), int(input())

def printcount(mm: int, nn: int):
    for i in range(mm, nn + 1):
        print(f'{i}')

printcount(m, n)
