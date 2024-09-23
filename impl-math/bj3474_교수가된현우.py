T = int(input())
for _ in range(T):
    N = int(input())

    cur = 5
    res = 0

    while cur <= N:
        res += N // cur
        cur *= 5

    print(res)
