N, M = map(int, input().split())

tmp = list(map(int, input().split()))
langs = [0] + tmp

nodes = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

ans = 1
v = []

for i in range(1, 11):
    v = [False for _ in range(N + 1)]

    def dfs(cur, lang):
        v[cur] = True

        for j in nodes[cur]:
            if not v[j] and langs[j] in [langs[1], lang]:
                dfs(j, lang)

        return v.count(True)

    ans = max(ans, dfs(1, i))


print(ans)
