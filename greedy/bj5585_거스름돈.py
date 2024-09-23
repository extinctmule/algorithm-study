"""
모든 잔돈이 나눠떨어지므로 그리디 가능
"""

cost = 1000 - int(input())
ans = 0

for coin in [500, 100, 50, 10, 5, 1]:
    if cost >= coin:
        ans += cost // coin
        cost %= coin

print(ans)
