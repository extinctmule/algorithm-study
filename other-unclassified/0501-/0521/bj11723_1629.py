# def add(S, x):
#     if x not in S:
#         S.


# def remove(S, x):
#     if x in S:
#         S.remove(x)

import sys

M = int(sys.stdin.readline())  # int(input())
S = set()

for i in range(M):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 2:
        command, x = temp[0], temp[1]
        x = int(x)

        if command == "add":
            S.add(x)
        elif command == "remove":
            S.discard(x)
        elif command == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif command == "toggle":  # else만 해도 되긴 함
            if x in S:
                S.discard(x)
            else:
                S.add(x)

    else:
        if temp[0] == "all":
            # 굳이 (i for i in range(1, 21)) 쓰지 말고
            # list[range(1,21)] 로 적었다가, 틀림. ()로 해야함

            S = set(range(1, 21))
        elif temp[0] == "empty":
            S = set()  # S.clear()
