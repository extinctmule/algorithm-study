"""
10:08
세준이가 걷는방법:
1. 시간W 동안 가로세로 한블록
2. 시간S 동안 대각선
(0,0)에서 집인 (X,Y)로 가는 최소시간?

만약 2*W<=S면 그냥 항상 가로세로만 해도될듯
W<S<2*W 면 S다쓴후 나머지 가로세로.
S<=W면 S만
"""

X, Y, W, S = map(int, input().split())

ans = 0

if 2 * W <= S:
    ans = W * (X + Y)
else:
    ans = S * min(X, Y)
    tmp = abs(X - Y)

    if W < S:
        ans += W * tmp
    else:
        if tmp % 2 == 0:
            ans += S * tmp
        else:
            ans += S * (tmp - 1) + W

print(ans)
