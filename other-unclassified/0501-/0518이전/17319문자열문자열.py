sol = {0: "No", 1: "Yes"}

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    S = input()

    mid = N // 2
    res = 0

    if N != 1 and S[: mid - 1] == S[mid:]:
        res = 1

    print(f"{tc} {sol[res]}")
