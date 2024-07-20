"""
Length:         0  1  2  3  4   5   6   7   8   9  10
price_table = { 0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 };
"""

# func(6)하면 [1,1,1,1,1,1], [1,1,1,1,2], ... [6] 이렇게 리턴하는 함수 구현..가능? 가능하다면, N이 몇 이하일때까지 시간복잡도 쓸만함?


N = 10
# tags = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
tags = [0, 3, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# opt = [0 for _ in range(N + 1)]

# 실제 값은 1: 1~10, 2: 2~10, 3: 3~10 까지만 들어있다. dist[3][2] 이딴건 없음.
# dist = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# dist같은거 필요없음....
res = tags.copy()  # tags내의 int는 불변객체이므로 deepcopy말고 걍 copy해도됨

# 아래코드와 동일. 이거는 3 1, 2 2, 1,3이라면 아래는 1 3, 2 2, 3 1 인거임
# for i in range(1, N + 1):
#     imax = res[i]
#     for j in range(1, i):  # 인덱스 맞는지 확인
#         print(i - j, j)
#         imax = max(imax, res[i - j] + tags[j])
#     res[i] = imax


for i in range(1, N + 1):
    imax = res[i]

    for j in range(1, i):
        print(j, i - j)
        imax = max(imax, res[j] + tags[i - j])

    res[i] = imax


for i, v in enumerate(res):
    print(f"{i}: {v}")


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = len(lst)

trlst1 = [[lst[j][i] for j in range(N)] for i in range(N)]
trlst2 = [list(row) for row in zip(*lst)]


