"""Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.
Формат входных данных
В первой строке записано текстовое предложение, во второй — количество повторений.
Формат выходных данных
Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с новой строки."""

mystr = str(input()) # строка для вывода
count = int(input()) # сколько раз повторять

def strToCount(s: str, c: int):
    # повторяет строку s количество раз c
    for _ in range(c):
        print(f'{s}')

strToCount(mystr, count)
