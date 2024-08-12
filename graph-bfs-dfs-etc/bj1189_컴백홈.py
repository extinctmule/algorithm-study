"""
1:30~
인덱스 그대로사용
T는 못가는부분
RxC

출력: 거리K만에 갈수있는 경로 경우의수
"""

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(input()) for _ in range(N)]


def dfs(x, y, cnt):
    if cnt == K and x == 0 and y == M - 1:
        return 1
    ans = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == ".":
            grid[nx][ny] = "T"
            ans += dfs(nx, ny, cnt + 1)
            grid[nx][ny] = "."
    return ans


grid[N - 1][0] = "T"
print(dfs(N - 1, 0, 1))
