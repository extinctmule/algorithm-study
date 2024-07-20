import sys


def dp(i, w):
    if i == N:
        return 0
    if arr[i][w]:  # 값 존재하면
        return arr[i][w]

    put = 0
    if w + catalog[i][0] <= K:
        put = catalog[i][1] + dp(i + 1, w + catalog[i][0])

    skip = dp(i + 1, w)

    arr[i][w] = max(put, skip)

    return arr[i][w]


input = sys.stdin.readline

N, K = map(int, input().split())

# 인덱스 0부터 사용
catalog = [[0, 0] for _ in range(N)]  # 무게, 가치

for i in range(N):
    catalog[i][0], catalog[i][1] = map(int, input().split())

arr = [[0 for _ in range(K + 1)] for _ in range(N)]

print(dp(0, 0))
