"""
N개행 M개열
     1   2  3  4 ... M
1 구름집
2
3
...
N                    탈출구

각 칸은 2(땅), 1(하늘), 0(쑥대밭)

칸이동 1초
하늘 거칠때는 날아가야하는데 에너지소모. 땅에서 '쉴'때마다 1씩 에너지충전.
항상 0<=에너지<=K 상태.

주의: 구하는것은 에너지K의 최소값
시간이 더 오래걸려도 땅으로만, 또는 하늘제일 적게 디디는 곳을 구해야함
"""

N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
q = [(0, 0, 0)]  # i,j,에너지(하늘 수)
v = [[0 for _ in range(M)] for _ in range(N)]  #

ans = N * M

while q:
    ci, cj, ck = q.pop(0)

    if ci == N - 1 and cj == M - 1 and ck <= T:  # T초 어떻게체크?
        ans = min(ans, ck)

    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + i, cj + j
        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != 0 and v[ni][nj] == 0:
            if grid[ni][nj] == 1 and ck >= 1:
                ck -= 1
                if ck < 0:
                    if grid[ci][cj] == 2:
                        ck += 1
                        q.append((ni, nj, ck))
                        v[ni][nj] = v[ci][cj] + 2
            q.append((ni, nj, ck))
            v[ni][nj] = v[ci][cj] + 1

if ans == N * M:
    print(-1)
else:
    print(ans)
