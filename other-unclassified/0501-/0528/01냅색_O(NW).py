# 시간초과 뜸

# catalog = [[6, 3], [5, 2], [3, 1]]  # 가치, 무게
# catalog = [[0, 0], [10, 4], [40, 3], [20, 2], [30, 1]]
# catalog = [[0, 0], [30, 1], [20, 2], [40, 3], [10, 4]]
import sys

input = sys.stdin.readline

N, W = map(int, input().split())
catalog = [[0, 0] for _ in range(N + 1)]
for i in range(1, N + 1):
    catalog[i][0], catalog[i][1] = map(int, input().split())

arr = [[0 for _ in range(W + 1)] for _ in range(N + 1)]


for i in range(0, N + 1):
    weight, val = catalog[i][0], catalog[i][1]
    for j in range(0, W + 1):
        arr[i][j] = max(arr[i][j], arr[i - 1][j])  # 아이템 안 넣음.수직으로 내려감.

        if j + weight <= W:
            # 넣고 무게 추가
            arr[i][j + weight] = max(arr[i][j + weight], arr[i - 1][j] + val)

# for a in arr:
#     print(a)
