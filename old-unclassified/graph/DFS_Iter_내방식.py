# 억지로 구현해본 DFS. 인접행렬 사용. 인접리스트쓰는게 더편할거같음..
# 정점 번호가 작은 것을 먼저 방문하자.
N, M, V = map(int, input().split())

# [[0]*N]*N 하면 안됨. * 연산자로 배열 선언하면 shallow copy가 됨
mat = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    mat[v1][v2] = 1
    mat[v2][v1] = 1


# DFS(틀림)
res = [V]
cur = V
for _ in range(N):
    temp = [i for i, value in enumerate(mat[cur]) if value == 1]

    for t in temp:
        # temp = mat[cur].index(1)
        if t not in res:
            res.append(t)
            cur = t

print(" ".join(map(str, res)))
