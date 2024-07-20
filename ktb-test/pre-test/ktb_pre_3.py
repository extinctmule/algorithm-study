
def dfs(i):
    v.add(i)
    for adj in graph[i]:
        if adj not in v:
            dfs(adj)

N, M = map(int, input().split())
# 인덱스 1부터
edges= [tuple(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
for u, v in edges:
    graph[u].append(v)

#set 주의
v = set()
ans = 0


for i in range(1, N + 1):
    if i not in v:
        v.clear()
        dfs(i)
        ans = max(ans, len(v))

print(ans)#줄바꿈O