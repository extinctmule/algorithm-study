'''
11:17~
1<=M,N,K <=100
세로M x 가로N
분리된 영역의 넓이가 0인 경우는 없다.
왼쪽아래, 오른쪽위 꼭짓점으로 주어짐.
제1사분면 느낌으로 생각하면될듯. 인덱스 0 시작.

색칠안된곳을 bfs갈수있는곳으로 1, 색칠된곳을 갈수없는곳으로 0으로 두자.

'''
from collections import deque

def bfs(si,sj,grid,v):
    #v부터 체크
    if v[si][sj]:
        return 0
    q = deque([(si,sj)])
    v[si][sj]=1
    ci,cj = si,sj
    
    while q:
        ci, cj = q.popleft()
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = ci+i,cj+j
            if 0<=ni<M and 0<=nj<N and grid[ni][nj] and not v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1
    return v[ci][cj]
    
    
M,N,K = map(int,input().split())
grid = [[1]*N for _ in range(M)] #여기서 또 M,N바꿔써서 한번 틀렸음.
v = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):#grid[i][x1:x2] 도 됐던듯?
            grid[i][j] = 0
            v[i][j] = 1#이거 빼면 안됨


ans1 = 0
ans2 = []

for i in range(M):
    for j in range(N):
        tmp = bfs(i,j,grid,v)
        if tmp:
            ans1 += 1
            ans2.append(tmp)

print(ans1)
print(" ".join(map(str,ans2.sort())))