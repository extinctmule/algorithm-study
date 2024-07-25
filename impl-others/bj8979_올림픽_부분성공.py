#구현, 정렬
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
scores = []

for i in range(1, N + 1):
    country, G, S, B = map(int, input().split())
    # medals.append(list(map(int, input().split())))
    scores.append([country, int(100 * G + 10 * S + B)])

scores = sorted(scores, key=lambda x: x[1])
res = [1]

for i in range(1, N):
    if scores[i][1] == scores[i - 1][1]:
        res.append(res[i - 1])
    else:
        res.append(res[i - 1] + 1)

for i in range(N):
    if scores[i][0] == K:
        print(res[i])
        break