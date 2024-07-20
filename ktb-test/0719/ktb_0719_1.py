N,M,x = map(int, input().split())
trees = list(map(int, input().split()))
Q = int(input())
moves = list(map(str,input().split()))

x-=1
ans = 0

for i in range(Q):
	#print(trees[x]+1, M)
	if trees[x]+i >= M:
		ans += trees[x]+i
		trees[x] = -i
	
	if moves[i]=='L':
		if x==0:
			x=N-1
		else:
			x-=1
	elif moves[i]=='R':
		if x==N-1:
			x=0
		else:
			x+=1


print(ans)