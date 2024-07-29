def knapsack(N, W, items):
    arr = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for w in range(0, W + 1):
            if weight <= w:
                arr[i][w] = max(arr[i - 1][w], arr[i - 1][w - weight] + value)
            else:
                arr[i][w] = arr[i - 1][w]

    return arr[N][W]


import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 인덱스 0부터 사용
catalog = [[0, 0] for _ in range(N)]  # 무게, 가치

for i in range(N):
    catalog[i][0], catalog[i][1] = map(int, input().split())

print(knapsack(N, K, catalog))
