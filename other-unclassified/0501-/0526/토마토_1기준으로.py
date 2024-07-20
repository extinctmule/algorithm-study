import sys


def dfs(ci, cj, ck, tmp):
    v_dfs[ci][cj][ck] = 1
    tmp.append((ci, cj, ck))

    for i, j, k in mnh_list:
        ni, nj, nk = ci + i, cj + j, ck + k

        if (
            0 <= ni < H
            and 0 <= nj < N
            and 0 <= nk < M
            and arr[ni][nj][nk] != -1
            and v_dfs[ni][nj][nk] == -1
        ):
            dfs(ni, nj, nk, tmp)


def sol():
    connected = []

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not v_dfs[i][j][j]:
                    tmp = []
                    dfs(i, j, k, tmp)
                    connected.append(tmp)

    riped = []

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    riped.append((i, j, k))

    for i in range(M + N + H):  # 이거 맞음?

        for ci, cj, ck in riped:
            for i, j, k in mnh_list:
                ni, nj, nk = ci + i, cj + j, ck + k
                if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and arr[ni][nj][nk] == 0:
                    v[ni][nj][nk] = 1


input = sys.stdin.readline
M, N, H = map(int, input().split())
arr = []

# 방문거리. 리스트로 못하고 행렬으로해야할듯. 리스트로도 최단거리체크 할방법이있나?
v = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
v_dfs = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

mnh_list = (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)

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
