def solution(friends, gifts):
    N = len(friends)

    d = [0] * N  # 선물지수
    who = {}  # friend별 인덱스지정
    mat = [[0] * N for _ in range(N)]
    for i, f in enumerate(friends):
        d[i] = 0
        who[f] = i

    res = [0] * N
    for g in gifts:
        a, b = g.split()
        i, j = who[a], who[b]
        d[i] += 1
        d[j] -= 1
        mat[i][j] += 1

    for i in range(N):
        for j in range(i + 1, N):
            if mat[i][j] > mat[j][i]:
                res[i] += 1
            elif mat[i][j] < mat[j][i]:
                res[j] += 1
            else:
                if d[i] > d[j]:
                    res[i] += 1
                elif d[i] < d[j]:
                    res[j] += 1

    return max(res)


friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = [
    "alessandro brad",
    "alessandro joy",
    "alessandro conan",
    "david alessandro",
    "alessandro david",
]

print(solution(friends, gifts))
