"""Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
Программа должна вывести 10 раз текст «Python is awesome!», каждый на отдельной строке."""

def print10(mystr: str):
    for i in range(10):
        print(f'{mystr}')

s = 'Python is awesome!'

print10(s)