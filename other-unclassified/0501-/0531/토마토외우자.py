import sys
from collections import deque


def bfs():
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]

    unripe = 0
    # 익은 좌표 q에 추가
    # 안익은 개수 세기
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    q.append((h, i, j))
                    v[h][i][j] = 1
                elif arr[h][i][j] == 0:
                    unripe += 1

    hij_list = ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0))

    while q:
        ch, ci, cj = q.popleft()
        for h, i, j in hij_list:
            nh, ni, nj = ch + h, ci + i, cj + j

            if (
                0 <= nh < H
                and 0 <= ni < N
                and 0 <= nj < M
                and arr[nh][ni][nj] == 0
                and v[nh][ni][nj] == 0
            ):
                q.append((nh, ni, nj))
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                unripe -= 1

    if unripe == 0:
        return v[ch][ci][cj] - 1
    else:
        return -1


input = sys.stdin.readline
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(bfs())
