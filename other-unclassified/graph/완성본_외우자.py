import sys


# 위키피디아 버전 non-recursive
def dfs_iter(V):  # stack 이용
    s = [V]

    while s:
        V = s.pop()

        if not visited_dfs[V]:
            visited_dfs[V] = True
            res_dfs.append(V)

            # for i in range(N, 0, -1):  # 정점번호 작은것을 먼저 방문하기 위해
            for i in graph[V][::-1]:
                if not visited_dfs[i]:  # and i not in s:
                    s.append(i)


# stack 사용한거 말고, 이렇게 재귀로 푼 dfs가 dfs의 정의에 가장가까움.
def dfs(node):
    visited_dfs[node] = True
    res_dfs.append(node)

    for w in graph[node]:
        if not visited_dfs[w]:
            dfs(w)


# queue로 pop 해가면서 구현하기
def bfs(node):
    q = [node]
    res_bfs.append(node)

    while q:
        node = q.pop(0)
        for w in graph[node]:
            if not visited_bfs[w]:
                visited_bfs[w] = True
                res_bfs.append(w)
                q.append(w)


def bfs_noq(node):
    q = [node]
    visited_bfs[node] = True
    res_bfs.append(node)

    try:
        for i in range(0, N):
            node = q[i]
            for w in graph[node]:
                if not visited_bfs[w]:
                    res_bfs.append(w)
                    visited_bfs[w] = True
                    q.append(w)
    except:  # node = q[i] 여기에서 error가 나면,
        return


input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for node in graph:  # 작은번호부터 방문해야하므로 정렬 필수임
    node.sort()

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
res_dfs = []
res_bfs = []

dfs_iter(V)
bfs_noq(V)

print(" ".join(map(str, res_dfs)))
print(" ".join(map(str, res_bfs)))
