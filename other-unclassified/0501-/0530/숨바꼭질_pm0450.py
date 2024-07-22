def bfs(N, K):
    v = [0 for _ in range(200001)]
    q = []

    v[N] = 1
    q.append(N)

    while q:
        ci = q.pop(0)

        if ci == K:
            return v[ci]
        if K in (ci - 1, ci + 1, ci * 2):
            return v[ci] + 1

        for i in (-1, 1, ci):
            ni = ci + i
            if 0 <= ni and v[ni] == 0:
                v[ni] = v[ci] + 1
                if ni == K:
                    return v[ni]
                q.append(ni)


N, K = map(int, input().split())

if N > K:
    print(N - K)
else:
    print(bfs(N, K) - 1)
