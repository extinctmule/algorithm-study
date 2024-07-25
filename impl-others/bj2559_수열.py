#8:50~9:12
# 정수 수열. 연속합이 가장 큰 값 출력
# 전체 날짜수 N: 범위 1~100,000
# K:연속적인 날짜의 수

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# cumsum = [arr[0]]
# for i in range(1,N):
#     cumsum.append(cumsum[i-1]+arr[i])

# ans = cumsum[K-1]

# for i in range(K, N):
#     ans = max(ans,cumsum[i]-cumsum[i-K])

# print(ans)

ans = sum(arr[0:K])
pre = ans

for i in range(1, N-K+1):
    pre = pre-arr[i-1]+arr[i+K-1]
    ans = max(ans, pre)

print(ans)

'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3
'''