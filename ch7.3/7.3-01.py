"""На вход программе подаются два целых числа a и b (a ≤ b). Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b (включительно),
куб которых оканчивается на 4 или 9.
Формат входных данных
На вход программе подаются два целых числа a и b (a ≤ b).
Формат выходных данных
Программа должна вывести одно целое число в соответствии с условием программы.
Примечание. Куб числа aa – это его третья степень (a3)."""

a, b = int(input()), int(input())

# def some(aa: int, bb: int):
#     count = 0

#     for i in range(aa, bb + 1):
#         if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
#             count += 1
#     print(f'{count}')

def some(aa: int, bb: int) -> int:
    count: int = 0
    for i in range(aa, bb + 1):
        if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
            count += 1
    return count

print(some(a, b))
