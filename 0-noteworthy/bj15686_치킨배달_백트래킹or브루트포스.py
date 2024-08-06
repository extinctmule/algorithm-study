'''
12:26~
N*N인 도시
0빈칸 or 1집 or 2치킨집
(r,c) 그리고 인덱스 0부터 시작해도 될듯?
2<=N<=50
1<=M<=13
1<=집의개수<=2*N
M<=치킨집개수<=13
여기서, 모든집의 치킨거리의 합이 제일 작도록 하는 남겨둘 치킨집 M개 골라

출력: 그후 치킨거리의 최솟값


2500*100*?  <- 시간초과?
'''
from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

def dfs(a,b):
    global ans
    if a>len(chi):
        return
    if b==M:
        dists=0
        for r, c in hou:
            dist = (2*N)**2
            for i in q:
                rr,cc = chi[i]
                dist = min(dist, abs(rr-r)+abs(cc-c))
            dists+=dist
        ans = min(ans, dists)
        return
    q.append(a)
    dfs(a+1,b+1)
    q.popleft()
    dfs(a+1,b)
    

N, M = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

chi, hou, q = deque([]),deque([]), deque([])

for i in range(N):
    for j in range(N):
        if grid[i][j]==2:
            chi.append((i,j))
        elif grid[i][j]==1:
            hou.append((i,j))

ans = (2*N)**2
dfs(0,0)
print(ans)
