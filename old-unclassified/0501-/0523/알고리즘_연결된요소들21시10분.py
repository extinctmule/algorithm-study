def dfs(node, tmp):
    v[node] = 1
    tmp.append(node)

    for a in arr[node]:
        if not v[a]:
            dfs(a, tmp)


N = int(input())
pairs = int(input())

arr = [[] for _ in range(N)]
v = [0 for _ in range(N)]
res = []

for _ in range(pairs):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


for i in range(N):
    if not v[i]:
        tmp = []
        dfs(i, tmp)
        res.append(tmp)

print(f"{len(res)} components")
for i, tmp in enumerate(res):
    print(f"Components {i+1}:", *tmp)

"""
index 0부터 사용
arr로
모든 정점 순서대로 dfs 하되,
visited된 정점은 건너뛰면 됨
res= [] 를 각각 parameter로 넘기며 append하자

13
13
0 1
0 2
0 5
0 6
3 4
3 5
4 5
4 6
7 8
9 10
9 11
9 12
11 12




"""
