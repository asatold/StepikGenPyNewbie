import math
n: int = int(input())

def some(nn: int) -> int:
    count: int = 0
    for i in range(1, nn + 1):
        count += 1 / i
    return count - math.log(nn)

print(f'{some(n)}')
