# 주의: Ri와 Ci는 다 1이상!! 1~N
N,M,K = map(int, input().split())
dists = [[0]*(M+1) for _ in range(N+1)]# 거리
pandas = [[0,0] for _ in range(K)]#판다 좌표
pcheck = [[False]*(M+1) for _ in range(N+1)]# True면 판다있는칸


for i in range(K):
	pi, pj = map(int, input().split())
	pandas[i] = [pi,pj]
	pcheck[pi][pj] = True

#인덱스 0 무시하고 루프돌기.
for pi, pj in pandas:
	for i in range(1, N+1):
		tmp = (pi-i)**2
		for j in range(1,M+1):
			if not pcheck[i][j]:
				dists[i][j] += tmp + (pj-j)**2

ans = ((N**2)+(M**2))*K
for i in range(1,N+1):
	for j in range(1,M+1):
		if not pcheck[i][j]:
			ans = min(ans,dists[i][j])
			
print(ans)

