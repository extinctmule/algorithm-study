T = int(input())

for i in range(1, T + 1):
    A, B, C = map(int, input().split())

    res = 0
    if B <= 1 or C <= 2:
        print(f"#{i} -1")
        continue
    if B >= C:
        res += B - C + 1
        B = C - 1
    if A >= B:
        res += A - B + 1
        A = B - 1

    # if A <= 0:
    #     print(f"#{i} -1")
    #     continue

    print(f"#{i} {res}")
