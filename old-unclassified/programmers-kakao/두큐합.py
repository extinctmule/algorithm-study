#무시. 틀린코드 틀린접근
from collections import deque


def bfs(q1, q2, goal):
    n = len(q1)
    q1 = deque(q1)  # 가능?
    q2 = deque(q2)

    q = deque()
    v = deque()  # 계산속도위해 q1만저장하자
    q.append([q1, q2])
    v.append(q1)
    res = deque()
    res.append(0)
    limit = 0
    while q:
        if limit>
        c1, c2 = q.popleft()
        if sum(c1) == goal:
            return res[v.index(c1)]

        if c1:
            n1, n2 = c1.copy(), c2.copy()
            n2.append(n1.popleft())
            if n1 not in v:
                q.append([n1, n2])
                v.append(n1)
                res.append(res[v.index(c1)] + 1)

        if c2:
            n1, n2 = c1.copy(), c2.copy()
            n1.append(n2.popleft())
            if n1 not in v:
                q.append([n1, n2])
                v.append(n1)
                res.append(res[v.index(c1)] + 1)

    return -1


def solution(queue1, queue2):
    s = sum(queue1) + sum(queue2)

    if s % 2:
        return -1

    return bfs(queue1, queue2, s // 2)


print(solution([1, 4], [4, 8]))
# printsolution([3, 2, 7, 2], [4, 6, 5, 1])
