"""Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до
Формат входных данных
На вход программе подается одна строка текста.
Формат выходных данных
Программа должна вывести десять строк в соответствии с условием задачи."""

mystr: str = input()

def countmystr(s: str):
    for i in range(10):
        print(f'{i} {s}')

countmystr(mystr)