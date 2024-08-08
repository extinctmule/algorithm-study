from itertools import combinations
from collections import deque
import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

chi, hou = deque([]),deque([])

for i in range(N):
    for j in range(N):
        if grid[i][j]==2:
            chi.append((i,j))
        elif grid[i][j]==1:
            hou.append((i,j))
            
ans = (2*N)**2

for lst in combinations(chi,len(chi)-M):# 없앨집선택한것.
    c = copy.deepcopy(chi)
    
    for i, j in lst:
        c.remove((i,j))
    
    dist = 0
    
    for i,j in hou:
        d = 2*N
        for k,l in c:
            d = min(d,abs(i-k)+abs(j-l))
        
        dist+=d
    ans = min(ans, dist)

print(ans)