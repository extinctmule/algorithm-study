def dfs(node):
    v[node] = 1  # 방문 확인 = 1
    sick.append(node)
    for i in edges[node]:
        if not v[i]:
            dfs(i)


# index 1부터 하자. 0은 무시
N = int(input())
pair = int(input())
edges = [[] for _ in range(N + 1)]

for _ in range(pair):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(N):
    edges[i].sort()

v = [0] * (N + 1)
v[1] = 1
sick = []
dfs(1)
print(len(sick) - 1)