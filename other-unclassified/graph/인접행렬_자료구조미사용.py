# bj1260
# 인접행렬로 구현
# 제약사항: 정점 번호가 작은 것을 먼저 방문하자.


def dfs(V):
    visited1[V] = True
    res1.append(V)

    for i in range(1, N + 1):
        if mat[V][i] == 1 and not visited1[i]:
            dfs(i)
            # return 하면 "틀림" 실수함..


# 위키피디아 버전 non-recursive
def dfs_iter(V):  # stack 이용
    s = [V]

    while s:
        V = s.pop()

        # res1.append(V)
        if not visited1[V]:
            visited1[V] = True
            for i in range(N, 0, -1):  # 정점번호 작은것을 먼저 방문하기 위해
                if mat[V][i] and not visited1[i]:
                    s.append(i)
                    # visited1[i] = True
            res1.append(V)


# queue안쓰고 구현 시도
def bfs(V):
    visited2[V] = True
    res2.append(V)
    j = 0
    while j < len(res2):
        V = res2[j]
        for i in range(1, N + 1):
            if mat[V][i] == 1 and not visited2[i]:
                visited2[i] = True
                res2.append(i)
        j += 1


N, M, V = map(int, input().split())

# [[0]*N]*N 처럼 하면 안됨. * 연산자로 배열 선언하면 shallow copy가 됨
mat = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    mat[v1][v2] = 1
    mat[v2][v1] = 1

visited1 = [False] * (N + 1)  # dfs용
visited2 = [False] * (N + 1)  # bfs용
res1 = []
res2 = []

# DFS
dfs_iter(V)
bfs(V)

print(" ".join(map(str, res1)))
print(" ".join(map(str, res2)))

# print(" ".join(map(str, res)))
