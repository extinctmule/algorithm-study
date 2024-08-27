sum = 11
arr = [2, 3, 5]

dp = [-1] * (sum + 1)
dp[0] = 0

for i in range(1, sum + 1):
    cnt = float("inf")
    for coin in arr:
        if i - coin >= 0 and dp[i - coin] != -1:
            cnt = min(cnt, dp[i - coin] + 1)
    if cnt != float("inf"):
        dp[i] = cnt

print(dp)
