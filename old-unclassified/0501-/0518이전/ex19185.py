TC = int(input())

for tc in range(1, TC + 1):

    N, M = map(int, input().split())
    nlist = input().split()
    mlist = input().split()

    Q = int(input())
    qlist = [None] * Q

    for i in range(0, Q):
        qlist[i] = int(input())

    print(f"#{tc}", end="")
    for q in qlist:
        print(" " + nlist[(q + N - 1) % N] + mlist[(q + M - 1) % M], end="")

    print()
