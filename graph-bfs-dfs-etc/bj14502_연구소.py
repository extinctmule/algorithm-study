'''
2:22~3:45
바이러스 확산 막기위해 벽을 세우자!
연구소: 세로N x 가로M.  3<=N,M<=8
0:빈칸, 1:벽, 2:바이러스 2<=2의개수<=10

딱 3개 벽 세워야함.
안전영역이 최대가 되도록
그냥.. 0위치별로 벽을 모두세워보는거 따지는거밖에 방법을 모르겠음..
최대 62C3인데 가능?
62*61*60/6 는 대략 36000 에다가 거기에 bfs를...해보자
'''
import copy
from collections import deque
from itertools import combinations

def bfs(si,sj,gc,v):
    q = deque([[si,sj]])
    v[si][sj]=True
    cnt = 0 #2자신은 제외. 0에서 2가된것들만
    
    while q:
        ci,cj = q.popleft()
        
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni,nj = ci+di,cj+dj
            if 0<=ni<H and 0<=nj<W and gc[ni][nj]==0 and v[ni][nj]==False:
                q.append([ni,nj])
                v[ni][nj]=True
                cnt+=1
    return cnt

H,W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]#[map(int, input().split())] 이 아니라,


# 0,2의 위치집합 만드셈
zeros = []
twos = []
for i in range(H):
    for j in range(W):
        if grid[i][j]==0:
            zeros.append([i,j])
        elif grid[i][j]==2:
            twos.append([i,j])

zero = len(zeros)-3
ans = 0
for lst in combinations(zeros,3):
    gc = copy.deepcopy(grid)
    for i,j in lst:# 벽3개 세워라
        gc[i][j] = 1
        
    zerotwo=0# 0에서 2가된 애들
    v = [[False]*W for _ in range(H)]
    for i,j in twos:#갈수있는곳 2로 다 채워라
        zerotwo += bfs(i,j,gc,v)
    ans = max(ans,zero-zerotwo)

print(ans)