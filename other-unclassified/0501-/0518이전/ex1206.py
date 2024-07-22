for tc in range(1, 11):
    N = int(input())
    nlist = list(map(int, input().split()))
    ans = 0

    for i in range(2, N - 2):
        l = max(nlist[i - 2], nlist[i - 1])
        r = max(nlist[i + 1], nlist[i + 2])
        tmp = nlist[i] - max(l, r)

        if tmp > 0:
            ans += tmp

    print(f"#{tc} {ans}")
