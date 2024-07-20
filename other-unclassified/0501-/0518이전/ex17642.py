T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    num = B - A
    res = 0

    if num == 0:
        res = 0
    elif num < 0 or num == 1:
        res = -1
    else:
        if num % 2:
            res = 1 + (num - 3) // 2
        else:
            res = num // 2

    print(f"#{tc} {res}")
