import sys


def bfs(v, q, si, sj, sk):

    v[si][sj][sk] = 1
    q.append((si, sj, sk))

    mnh_list = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))

    while q:
        ci, cj, ck = q.pop(0)
        v_c = v[ci][cj][ck]

        for i, j, k in mnh_list:
            ni, nj, nk = ci + i, cj + j, ck + k

            if (
                0 <= ni < H
                and 0 <= nj < N
                and 0 <= nk < M
                and arr[ni][nj][nk] == 0
                and not v[ni][nj][nk]
            ):
                # if not v[ni][nj][nk]:
                #     v[ni][nj][nk] = v_c + 1
                #     q.append((ni, nj, nk))
                # else:
                #     v[ni][nj][nk] = min(v[ni][nj][nk], v_c + 1)
                v[ni][nj][nk] = v_c + 1
                q.append((ni, nj, nk))

                # for ii in range(H):
                #     for jj in range(N):
                #         for kk in range(M):
                #             print(v[ii][jj][kk], end=" ")
                #         print()
                # print()


def sol():
    # 방문거리. 리스트로 못하고 행렬으로해야할듯. 리스트로도 최단거리체크 할방법이있나?
    v = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

    unripe = 0

    for grid in arr:
        for row in grid:
            for item in row:
                if item == 0:
                    unripe += 1

    if not unripe:
        print(0)
        return

    q = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:  # 이번엔 1에 대해 bfs해보자.
                    bfs(unripe, q, i, j, k)

    res = 0
    for grid in arr:
        for row in grid:
            if 0 in row:
                print(-1)
                return
            res = max(res, max(row))

    print(res - 1)


input = sys.stdin.readline
M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

sol()


"""
import sys
from collections import deque


def bfs(q, v):
    unripe = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                # 이번엔 1에 대해 bfs해보자< NO!! queue에먼저 1들 추가하고 bfs돌리는거임.
                if arr[i][j][k] == 1:
                    v[i][j][k] = 1
                    q.append((i, j, k))
                elif arr[i][j][k] == 0:
                    unripe += 1

    mnh_list = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

    while q:
        ci, cj, ck = q.popleft()

        for i, j, k in mnh_list:
            ni, nj, nk = ci + i, cj + j, ck + k

            if (
                0 <= ni < H
                and 0 <= nj < N
                and 0 <= nk < M
                and arr[ni][nj][nk] == 0
                and v[ni][nj][nk] == 0
            ):
                v[ni][nj][nk] = v[ci][cj][ck] + 1
                q.append((ni, nj, nk))
                unripe -= 1

    if unripe == 0:
        return v[ci][cj][ck] - 1
    else:
        return -1


def sol():
    # 기본리스트로풀어서 계속 시간초과뜸
    # 지금처럼 큐에 삽입할 개수가 많은 경우에는 덱을 사용하셔야 시간초과가 나지 않습니다. 기본리스트를 사용하는 경우(O(n)) 보다 빠른(O(1)) 접근이 가능하기 때문입니다
    q = deque()
    v = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

    print(bfs(q, v))


input = sys.stdin.readline
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

sol()


"""
