# Kosaraju 알고리듬으로 선형시간 O(V+E)로 강연결요소들을 찾을 수 있습니다.


def dfs(node, tmp):
    v[node] = 1
    tmp.append(node)

    for i in range(N):
        if arr[node][i]:  # node와 i가 이어져있으면,
            if not v[i]:  # 그리고 아직 방문안했으면,
                dfs(i, tmp)


# index 0부터 시작
N = int(input())
pairs = int(input())

# 인접 행렬
arr = [[0 for _ in range(N)] for _ in range(N)]
v = [0 for _ in range(N)]
sc = []

for _ in range(pairs):
    a, b = map(int, input().split())
    arr[a].append(b)

# 뒤집기

# tmp만들고 순서대로 탐색 후 묶인애들 sc에 넣기, v[]방문한애들은 스킵.
for i in range(N):
    if not v[i]:
        tmp = []
        dfs(i, tmp)
        sc.append(tmp)


print(f"{len(sc)} strong components")
for i, r in enumerate(sc):
    print(f"Strong component{i}:", *r)

"""
13
22
0 1
0 5
2 0
2 3
3 2
3 5
4 2
4 3
5 4
6 0
6 4
6 8
6 9
7 6
7 9
8 6
9 10
9 11
10 12
11 4
11 12
12 9

"""
