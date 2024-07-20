# 성공 코드
# 최단거리 걱정x 어차피 for돌면서 제일빨리 목적지도착하는거 먼저 return됨.
def bfs(si, sj, di, dj):
    q = []
    v = [[0] * M for _ in range(N)]

    v[si][sj] = 1
    q.append((si, sj))

    while q:  # 항상 목적지도달 가능한게 보장될경우, True로 둘 수 있음.
        ci, cj = q.pop(0)

        if (ci, cj) == (di, dj):  # 목적지체크할 코드 위치가 여기가 맞나?
            return v[ci][cj]

        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci + i, cj + j

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and not v[ni][nj]:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))


N, M = map(int, input().split())
#arr = [input().strip() for _ in range(N)]  # arr[][]=='1'주의. 1 아님
arr = [list(map(int, input())) for _ in range(N)] #또는 이렇게 하고 arr[][]==1
res = bfs(0, 0, N - 1, M - 1)  # -1 주의
print(res)
