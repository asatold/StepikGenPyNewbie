"""Знакочередующаяся сумма
1-2+3-4+5...
На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы"""

n = int(input())

# def znaksumm(nn: int) -> int:
#     count: int = 1
#     for i in range(2, nn + 1):
#         if i % 2 == 0:
#             count -= i
#         else:
#             count += i
#     return count

def znaksumm(nn: int) -> int:
    flag: bool = 0
    count: int = 0

    for i in range(1, nn + 1):
        if i == 1:
            count += i
        else:
            if flag == 0:
                count -= i
                flag = 1
            else:
                count += i
                flag = 0
    return count

print(f'{znaksumm(n)}')
