#bfs. 문어박사 유튜브영상 참고함
import sys
from collections import deque


def bfs():
    q = deque()
    unripe = 0
    mnh_list = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    q.append((i, j, k))
                elif arr[i][j][k] == 0:
                    unripe += 1

    while q:
        ci, cj, ck = q.popleft()

        for i, j, k in mnh_list:
            ni, nj, nk = ci + i, cj + j, ck + k

            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and arr[ni][nj][nk] == 0:
                arr[ni][nj][nk] = arr[ci][cj][ck] + 1
                q.append((ni, nj, nk))

                unripe -= 1

    if unripe == 0:
        return arr[ci][cj][ck] - 1
    else:
        return -1


input = sys.stdin.readline
M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(bfs())
