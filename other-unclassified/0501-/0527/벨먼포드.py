# bellmanford
import math

N = 5
edges = [[0, 1, 1], [1, 2, 5], [1, 3, 4], [2, 3, -3], [3, 4, 1], [4, 3, -100]]
E = len(edges)
dists = [math.inf for _ in range(N)]

source = 0
dists[source] = 0

# 최단경로의 지나가는 총 간선은 최대 N-1개
for _ in range(N - 1):
    for u, w, cost in edges:
        if dists[u] + cost < dists[w]:
            dists[w] = dists[u] + cost

    print(dists)

# 음의 사이클 체크
negcycle = False
for u, w, cost in edges:
    if dists[u] + cost < dists[w]:
        negcycle = True
        break

print(negcycle)
