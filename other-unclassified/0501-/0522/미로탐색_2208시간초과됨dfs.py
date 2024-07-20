# bj2178
import sys

sys.setrecursionlimit(10**6)


def dfs(r, c, count):
    if r < 0 or r >= row or c < 0 or c >= col:  # 인덱스 벗어난 경우
        return

    if mat[r][c] == "1":
        # 예전에 방문했었는데, 이번방문이 더 긴 경로로 온 경우 중단
        if visited[r][c] != 0 and count >= visited[r][c]:
            return

        # 첫방문이거나 이번 count가 더 짧을 경우 계속 탐색
        visited[r][c] = count

        if r == row - 1 and c == col - 1:
            res.append(count)
            return

        dfs(r, c + 1, count + 1)
        dfs(r + 1, c, count + 1)
        dfs(r, c - 1, count + 1)
        dfs(r - 1, c, count + 1)


input = sys.stdin.readline

row, col = map(int, input().split())
mat = ["" for _ in range(row)]
visited = [[0 for _ in range(col)] for _ in range(row)]
res = []

for i in range(row):
    mat[i] = input().strip()

dfs(0, 0, 1)

print(min(res))
