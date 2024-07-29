def hide_seek(res, i):
    if i == K:
        return res
    if K in (i - 1, i + 1, i * 2):
        return res + 1
    if i > K:
        res += i - K
        return res
    while i * 2 <= K:
        res += 1
        i *= 2

    walk = hide_seek(res + 1, i + 1)
    moonwalk = hide_seek(res + 1, i - 1)
    tp = hide_seek(res + 1, i * 2)

    return min(tp, walk, moonwalk)


N, K = map(int, input().split())

print(hide_seek(0, N))
