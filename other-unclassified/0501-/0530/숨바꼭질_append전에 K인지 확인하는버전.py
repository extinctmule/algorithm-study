def bfs(N, K):
    v = [-1] * (100001)
    q = []

    v[N] = 0
    q.append(N)

    while q:
        ci = q.pop(0)

        if ci == K:
            return v[ci]

        if K in (ci - 1, ci + 1, ci * 2):
            return v[ci] + 1

        for i in (-1, 1, ci):
            ni = ci + i
            # <= 100000 이거 안해줘서 계속 런타임에러(인덱스에러)뜸
            if 0 <= ni <= 100000 and v[ni] == -1:
                v[ni] = v[ci] + 1
                if ni == K:
                    return v[ni]
                q.append(ni)


N, K = map(int, input().split())

if N >= K:
    print(N - K)
else:
    print(bfs(N, K))
