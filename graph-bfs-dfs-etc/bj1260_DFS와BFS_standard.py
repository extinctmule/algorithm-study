
# 노드 별 인접리스트 사용, deque 자료구조 사용.
from collections import deque

def dfs(node):
    visited_dfs[node] = True
    dfs_list.append(node)
    for i in graph[node]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(node):
    queue = deque()
    visited_bfs[node] = True
    queue.append(node)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited_bfs[i]:
                queue.append(i)
                bfs_list.append(i)
                visited_bfs[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for node in graph:
    node.sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
dfs_list,bfs_list = [], [v]

dfs(v)
bfs(v)
print(*dfs_list)
print(*bfs_list)
