def bfs(si, sj, count):
    q = []
    v[si][sj] = 1
    q.append((si, sj))

    while q:
        ci, cj = q.pop(0)

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + i, cj + j
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and arr[ni][nj]:
                v[ni][nj] = 1  # v[ci][cj] + 1 말고 걍 1로 해도 됨
                count += 1
                q.append((ni, nj))

    return count


# 인덱스 0 시작으로 구현하자.
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
res = []  # 단지별 집의 수 리스트

for i in range(N):
    for j in range(N):
        if not v[i][j] and arr[i][j] == 1:
            res.append(bfs(i, j, 1))


res.sort()
print(len(res))
for r in res:
    print(r)