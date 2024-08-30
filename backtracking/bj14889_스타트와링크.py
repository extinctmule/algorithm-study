"""
N명(짝수)이
스타트 팀과 링크 팀으로 나뉨
능력치는 1~100 사이 정수
N=4이면
12 21 + 34 43

N=6이고 1,2,3 4,5,6 나뉘면
12 13 21 23 31 32 + ...
"""


def cal(alst, blst):
    asum, bsum = 0, 0
    for i in range(M):
        for j in range(M):
            asum += arr[alst[i]][alst[j]]
            bsum += arr[blst[i]][blst[j]]
    return abs(asum - bsum)


def dfs(n, alst, blst):
    global ans
    if n == N:  # 종료조건
        if len(alst) == len(blst):
            ans = min(ans, cal(alst, blst))
        return
    dfs(n + 1, alst + [n], blst)  # a팀 선택
    dfs(n + 1, alst, blst + [n])  # b팀 선택


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

M = N // 2
ans = 100 * M * M
dfs(0, [], [])

print(ans)
