# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 가로 M 세로 N
# 가로와 세로로 평행하게 "각각" K번씩 잘라서 (K+1)^2 조각으로.

#자르는 방법
# (x,y)하나 고르고 그걸로 가로1세로1자르는것.

#흠.. 일단 자르는중간에 재지말고, 다 자른다음 젤큰거 젤작은거 재자.
#시간복잡도는 N^2 이하 가능

# input
N,M,K = map(int, input().split())

#양끝값 0, M과 0,N 추가해주자.
arr_x, arr_y = [0 for _ in range(K+2)], [0 for _ in range(K+2)]

arr_x[0], arr_x[K+1] = 0,M
arr_y[0], arr_y[K+1] = 0,N

for i in range(1,K+1):
    arr_x[i], arr_y[i] = map(int, input().split())

arr_x.sort()
arr_y.sort()

gap_x, gap_y = [0 for _ in range(K+1)], [0 for _ in range(K+1)]

for i in range(K+1):
    gap_x[i] = arr_x[i+1]-arr_x[i]
    gap_y[i] = arr_y[i+1]-arr_y[i]

print(min(gap_x)*min(gap_y), max(gap_x)*max(gap_y), end='')
