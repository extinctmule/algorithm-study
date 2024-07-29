def dfs(node):
    v[node] = 1
    print(node, end=" ")
    for a in arr[node]:
        if a == first:
            print(node, a, "it has cycle")
        if not v[a]:
            dfs(a)


N = int(input())
pairs = int(input())

arr = [[] for _ in range(N)]
v = [0 for _ in range(N)]

first = 1

for _ in range(pairs):
    a, b = map(int, input().split())
    arr[a].append(b)

dfs(first)
