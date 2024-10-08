"""
1~N번 나라
M개 항로
1~10개 나라별 랜덤언어 알아야만 방문가능.
구름이는 1번나라 언어만 알고있음.

언어하나 추가 공부한후 방문할수있는 서로다른 나라의 최대 개수?(1번나라 포함)

인덱스 1부터사용. 배열크기 N+1
체크: 방문여부에다가 언어여부까지 체크하면 됨.

6 6
3 5 5 7 7 3
1 2
2 3
4 1
4 5
2 5
2 6
"""

from collections import deque

N, M = map(int, input().split())

tmp = list(map(int, input().split()))
langs = [0] + tmp

nodes = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)


def bfs(lang):
    v = [False for _ in range(N + 1)]
    q = deque([])

    v[1] = True
    q.append(1)
    res = 1

    while q:
        cur = q.popleft()
        for i in nodes[cur]:
            if v[i] == False and langs[i] in [lang, langs[1]]:
                v[i] = True
                q.append(i)
                res += 1

    return res


ans = 1
v = []

for i in range(1, 11):  # in langs로 할 수도 있는듯..
    v = [False for _ in range(N + 1)]
    ans = max(ans, bfs(i))

print(ans)
