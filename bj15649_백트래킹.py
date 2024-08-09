"""
엣지케이스 따로없는듯?
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, 10)]
v = [False for _ in range(N)]
maps = [0 for i in range(M)]


def dfs(d):
    if d >= M:  # 종료조건
        for i in range(M):
            print(maps[i], end=" ")
        print()
        return
    for i in range(0, N):
        if v[i]:
            continue
        v[i] = True
        maps[d] = arr[i]

        dfs(d + 1)
        v[i] = False


dfs(0)
