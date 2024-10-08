def bfs(node):
    q = []
    v = [0 for _ in range(N + 1)]  # 실수많이함.외우자

    v[node] = 1
    q.append(node)

    while q:
        node = q.pop(0)

        if node == B:
            return v[node]

        for i in arr[node]:
            if not v[i]:
                v[i] = v[node] + 1
                q.append(i)


N = int(input())
A, B = map(int, input().split())
pairs = int(input())

# 인덱스 1부터.
arr = [[] for _ in range(N + 1)]

for _ in range(pairs):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

res = bfs(A)

if res:
    print(res-1)
else:
    print(-1)


#또는, 걍 res 선언하지말고 아래와 같이도 가능.
'''
try:
    print(bfs(A) - 1)
except:
    print(-1)

'''