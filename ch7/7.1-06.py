"""На вход программе подается натуральное число n. Напишите программу, которая для каждого из чисел от 0 до n (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
Формат входных данных
На вход программе подается натуральное число n."""

count = int(input())

def squareInt(x: int):
    for i in range(x + 1):
        print(f'Квадрат числа {i} равен {i ** 2}')

squareInt(count)
