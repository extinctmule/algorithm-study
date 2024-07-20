
'''
test case
5
4 7
6 13
4 8
3 6
5 12

3 4
4 104
4 104
3 103

4 1
1 11
1 44
1 22
1 33

4 1
2 102
2 102
4 104
3 103

4 5
3 13
3 16
2 15
1 1

'''

N, K = int(input().split())

items = [[0,0]] # 인덱스 1부터로 맞추기 위해 하나 넣어놓음
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    w,v = int(input().split())
    items.append([w,v])

for i in range(1, N+1):
    for j in range(1,K+1):
        if dp[i][:]





bag = dict()

#bag = sorted(bag.items(), key=lambda x: x[0])#무게기준 정렬



cur = []#튜플의 리스트
