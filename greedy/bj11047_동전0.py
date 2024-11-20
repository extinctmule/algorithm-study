N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
ans = 0

for i in range(N - 1, -1, -1):
    if arr[i] <= K:
        Q = K // arr[i]
        ans += Q

        K -= Q * arr[i]

    if K == 0:
        break
print(ans)
