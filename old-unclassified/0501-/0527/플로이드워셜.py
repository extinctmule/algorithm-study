import math


def floyd_warshall(graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if k not in (i, j) or i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


# 플로이드-워셜 구현할땐 보통 인접행렬 사용.
# 인접행렬이 bottom up 동적프로그래밍과 잘맞기때문

graph = [
    [0.0, 3.0, 8.0, math.inf, -4.0],
    [math.inf, 0.0, math.inf, 1.0, 7.0],
    [math.inf, 4.0, 0.0, math.inf, math.inf],
    [2.0, math.inf, -5.0, 0.0, math.inf],
    [math.inf, math.inf, math.inf, 6.0, 0.0],
]

N = len(graph)

floyd_warshall(graph)
for i in range(N):
    print(graph[i])
