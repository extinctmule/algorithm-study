import sys

sys.stdin = open("input.txt", "r")


def findNotMatch(nlist, start, last):
    for i in range(start, last + 1):
        if i != nlist[i]:  # 예외케이스 주의
            return i

    return -1


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    tmp = list(map(int, input().split()))

    nlist = [-1] + tmp + [0]  # 인덱스를 편하게 쓰기위해 size를 N+1+1로 만듬.

    storage = []
    empty = N + 1

    for i in range(1, N + 1):
        target = nlist.index(i)

        if i == target:
            continue
        if empty == N + 1:
            target = findNotMatch(nlist, 1, N)
            if target == -1:
                break

        nlist[i], nlist[empty] = nlist[empty], nlist[i]
        print(nlist)
        nlist[i], nlist[target] = nlist[target], nlist[i]

        storage.append(i)
        storage.append(target)
        empty = target

        print(nlist)

    if storage:
        print(len(storage))
        print(" ".join(map(str, storage)))
    else:
        print(0)
        print()
