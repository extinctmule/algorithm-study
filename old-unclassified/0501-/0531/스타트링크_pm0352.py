from collections import deque

F, S, G, U, D = map(int, input().split())

q = deque()
v = [0] * (F + 1)
q.append(S)
v[S] = 1

# U,D, 등에대한 예외처리 필요??

while q:
    ci = q.popleft()

    for i in (U, -D):
        ni = ci + i

        # 범위 실수: 0 안됨!!!!!
        if 1 <= ni <= F and v[ni] == 0:
            q.append(ni)
            v[ni] = v[ci] + 1

if v[G]:
    print(v[G] - 1)
else:
    print("use the stairs")
