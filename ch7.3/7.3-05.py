"""На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.
Входные данные
На вход программе подается натуральное число n, (n ≤ 12).

Примечание. Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть
n!=1⋅2⋅3⋅…⋅n"""

n: int = int(input())  # по условию n должно быть меньше или равно 12

def myfactorial(nn: int) -> int:
    count: int = 1
    if nn <= 12:
        for i in range(1, nn + 1):
            count *= i
        return count
    
print(f'{myfactorial(n)}')    
