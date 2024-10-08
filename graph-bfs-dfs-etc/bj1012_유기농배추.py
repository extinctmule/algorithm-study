'''
10:58~11:49
1이 배추있는땅, 0이 없는땅
지렁이는 상하좌우 이동가능

필요한 최소의 지렁이 수 출력
입력범위 2500
가로M, 세로N
배추있는땅 개수 K
전역변수 v[][] 로 방문한 땅 체크
bfs로 돌되, 시작땅이 방문안한 땅이면 ans+=1 하자
'''
from collections import deque

def bfs(si,sj,v):
    if v[si][sj]:# 이미 방문한땅이면
        return False
    
    q = deque()
    q.append([si,sj])
    v[si][sj] = True
    
    while q:
        ci, cj = q.popleft()
        
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and grid[ni][nj]==1 and v[ni][nj]==False:#이부분 ni <M, nj<N 으로 해놔서 틀림
                q.append([ni,nj])
                v[ni][nj]=True
    
    return True


T = int(input())
ans = []

for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0]*M for _ in range(N)]
    lst = []
    worm = 0
    v = [[False]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int,input().split())
        grid[y][x] = 1# grid[x][y]로 해서 틀렸음
        lst.append((y,x))

    for y,x in lst:
        if bfs(y,x,v):
            worm+=1

    ans.append(worm)

print("\n".join(map(str, ans)))


'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''
'''
2
'''