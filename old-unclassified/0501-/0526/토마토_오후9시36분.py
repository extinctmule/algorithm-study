import sys


def bfs(si, sj, sk):
    q = []

    # 방문거리. 리스트로 못하고 행렬으로해야할듯. 리스트로도 최단거리체크 할방법이있나?
    v = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

    v[si][sj][sk] = 0  # sol을 위해 0부터 시작으로 한다.
    q.append((si, sj, sk))

    mnh_list = (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)

    while q:
        ci, cj, ck = q.pop(0)
        v_c = v[ci][cj][ck]

        for i, j, k in mnh_list:
            ni, nj, nk = ci + i, cj + j, ck + k

            if (
                0 <= ni < H
                and 0 <= nj < N
                and 0 <= nk < M
                and arr[ni][nj][nk] != -1
                and v[ni][nj][nk] == -1  # 방문안한거 이렇게 표시
            ):

                v[ni][nj][nk] = v_c + 1
                q.append((ni, nj, nk))

                if arr[ni][nj][nk] == 1:
                    return v[ni][nj][nk]

    return -1


def sol():
    # res = {}  # 디버깅용
    res = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    tmp = bfs(i, j, k)

                    if tmp == -1:
                        print(-1)  # 하나라도 경로 못찾은경우
                        return

                    res.append(tmp)

    # print("res:", res)
    if not res:  # 0, 즉 안 익은것이 하나도 없었을경우(?)
        print(0)
    else:
        print(max(res))


input = sys.stdin.readline
M, N, H = map(int, input().split())
arr = []

has_ripe = False
has_unripe = False

for i in range(H):
    arr.append([])
    for j in range(N):
        arr[i].append(list(map(int, input().split())))
        if 1 in arr[i][j]:
            has_ripe = True
        if 0 in arr[i][j]:
            has_unripe = True

if has_ripe:
    if has_unripe:
        sol()
    else:
        print(0)
else:
    if has_unripe:
        print(-1)
    else:
        print("no way")
