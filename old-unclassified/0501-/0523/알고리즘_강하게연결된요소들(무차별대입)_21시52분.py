def dfs(i, tmp):
    v[i] = 1
    tmp.append(i)

    for j in arr[i]:
        if not v[j]:  # 첨에 실행시킬때 이거 빼먹었음..
            dfs(j, tmp)


# index 0부터 시작
N = int(input())
pairs = int(input())

arr = [[] for _ in range(N)]
cango = [[] for _ in range(N)]

for _ in range(pairs):
    a, b = map(int, input().split())
    arr[a].append(b)

for i in range(N):  # 모든노드에 대해 커넥트 찾음
    v = [0 for _ in range(N)]  # 매번 리셋
    tmp = []

    dfs(i, tmp)
    cango[i] = tmp

v = [0 for _ in range(N)]
res = []

# arr아니고 cango기준으로 강하게연결된그룹 res 만드는것임!! 실수주의
for i in range(N):
    tmp = []
    for j in cango[i]:
        if not v[j] and i in cango[j]:
            v[j] = 1
            tmp.append(j)

    if tmp:
        tmp.sort()
        res.append(tmp)

print("cango: ", cango)
# print("res: ", res)

print(f"{len(res)} strong components")
for i, r in enumerate(res):
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
