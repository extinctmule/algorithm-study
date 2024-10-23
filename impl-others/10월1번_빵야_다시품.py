"""
10:23~11:19

"""

N = int(input())
hps = list(map(int, input().split()))
ans = 0

carr = [1, 2, 3, 4]
c = 0
(1 + 4) * N
for hp in hps:
    q = hp // 10
    r = hp % 10

    res = q * 4

    while r > 0:
        r -= carr[c]
        c += 1
        if c >= 4:
            c -= 4
        res += 1

    ans += res

print(ans)
