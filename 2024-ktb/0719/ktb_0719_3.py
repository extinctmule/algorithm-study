# 틀린코드
from collections import deque

# 최단거리 찾기
# 다만 v에서 나타나는 거리는 시작점 포함하므로, 문제가의미하는거리보다 1크므로,-1해서 리턴하자.
def bfs(si,sj,di,dj):
	if (si,sj)==(di,dj):#다음손님태우러가는 거리체크때매 이거 체크해줘야됨
		return 0
	
	q = deque()
	v = [[0]*N for _ in range(N)]
	
	q.append((si,sj))
	v[si][sj] = 1# 실은 0이지만 구현을 위해서 1로 설정.
	
	while q:
		ci, cj = q.popleft()
		
		if (ci,cj) == (di,dj):
			return v[ci][cj]-1#주의
		
		for i,j in [[0,1], [0,-1], [1,0],[-1,0]]:
			ni, nj = ci+i, cj +j
			if 0<=ni<N and 0<=nj<N and graph[ni][nj]==0 and v[ni][nj]==0:# 이동가능한지역이며, 안가본지역일경우
				q.append((ni,nj))
				v[ni][nj] = v[ci][cj]+1
	
	
	
N,M = map(int, input().split())
kibon,chuga,fee = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 문제에서 좌표 a,b,c,d는 1~N 까지다. graph등을 N+1로 쓰지 말고, a,b,c,d를 -1씩 해서 쓰자.
starts = [[0,0] for _ in range(M)]
ends = [[0,0] for _ in range(M)]
ans = 0

for i in range(M):
	a,b,c,d = map(int, input().split())
	starts[i][0],starts[i][1],ends[i][0],ends[i][1] = a-1,b-1,c-1,d-1

for i in range(M):
	#손님태워서 보내드려
	d = bfs(starts[i][0], starts[i][1], ends[i][0],ends[i][1])
	if d:
		ans += kibon - d*fee# 통행료는 항상

	if d>5:
		ans+= (d-5)*chuga

	#다음손님한테 가
	if i<M-1:
		d = bfs(ends[i][0],ends[i][1],starts[i+1][0],starts[i+1][1])
		ans-=d*fee


print(ans, end='')


'''
5 2
15 2 1
0 0 0 0 0
0 1 0 1 1
0 1 0 0 0
0 1 1 1 0
0 0 0 0 0
3 5 4 3
5 1 2 5

''' 