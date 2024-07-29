from itertools import combinations


def get_combinations(order):
    n = len(order)
    table = [[] for _ in range(n)]

    # 조합 생성
    for i in range(1, n + 1):
        comb = combinations(order, i)
        table[i - 1] = ["".join(c) for c in comb]

    return table


order = "ABCD"
combinations_table = get_combinations(order)
print(combinations_table)
