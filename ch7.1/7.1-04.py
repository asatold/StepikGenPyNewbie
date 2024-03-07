"""
Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
AAA
AAA
AAA
AAA
AAA
AAA
BBBB
BBBB
BBBB
BBBB
BBBB
E
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
G
"""

def print_abetg():
    i: int = 3
    for _ in range(6):
        print(f'A' * i)
    i += 1
    for _ in range(5):
        print(f'B' * i)
    i += 1
    print(f'E')
    for _ in range(9):
        print(f'T' * i) 
    print(f'G')

print_abetg()
