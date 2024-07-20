import sys

sys.stdin = open("input.txt", "r")


def findNotMatch(nlist, start, last):
    for i in range(start, last + 1):
        if i != nlist[i]:  # 예외케이스 주의
            return start

    return -1


def solve(storage):
    if storage:
        print(len(storage))
        print(" ".join(map(str, storage)))
    else:
        print(0)
        print()


TC = int(input())

for tc in range(1, TC + 1):
    print("tc:", tc)
    N = int(input())
    tmp = list(map(int, input().split()))
    nlist = [-1] + tmp + [0]  # 인덱스를 편하게 쓰기위해 size를 N+1+1로 만듬.

    storage = []
    empty = N + 1

    print("K0", nlist)
    # empty 자리를 처음 옮기는 과정
    i = findNotMatch(nlist, 1, N)

    if i == -1:  # 이미 정렬됨
        solve(storage)
        continue
    else:
        storage.append(i)
        nlist[i], nlist[empty] = nlist[empty], nlist[i]
        print("K1", nlist)
        empty = i

    count = 1

    for j in range(N):
        # 주의1. 실수함. 루프횟수는 i값과 상관없음. 아 이거걍 while(true)해도될거같은데..
        # if empty == N + 1: break# 주의2.실수함. empty==N+1로 종료조건 잘못설정함
        if empty == N + 1:
            target = findNotMatch(nlist, j, N)
            if target == -1:
                break
        else:
            target = nlist.index(empty)
        storage.append(target)
        nlist[target], nlist[empty] = nlist[empty], nlist[target]
        empty = target

        count += 1
        print(f"K{count}", nlist)

    solve(storage)
