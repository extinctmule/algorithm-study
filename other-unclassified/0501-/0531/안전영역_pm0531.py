from collections import deque
import sys


def bfs(si, sj, flood, v):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + i, cj + j

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > flood and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1


input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

set_h = set()
for row in arr:
    for item in row:
        set_h.add(item - 1)


max_h = 0
for row in arr:
    max_h = max(max_h, max(row))

res = []
# 1~ 최고높이-1 까지 비왔을때의 각각의 안전한영역개수를 res에 저장
for flood in set_h:  # range(1, max_h):
    v = [[0] * N for _ in range(N)]
    area = 0

    for si in range(N):
        for sj in range(N):
            if arr[si][sj] > flood and v[si][sj] == 0:  # v체크 주의.
                bfs(si, sj, flood, v)
                area += 1
    res.append(area)

print(max(res))
