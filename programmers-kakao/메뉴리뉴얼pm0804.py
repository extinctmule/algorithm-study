# from itertools import combinations


# def solution(orders, course):
#     answer = []
#     foodMap = [{} for _ in range(11)]  # [0],[1]은 쓰지 않는다
#     maxCnt = [0 for _ in range(11)]

#     # 오름차순정렬 싹다
#     for s in orders:
#         s = sorted(s)
#         for num in range(2, len(s) + 1):
#             for comb in combinations(s, num):
#                 key = "".join(comb)
#                 if key not in foodMap[num]:  # 없으면 추가
#                     foodMap[num][key] = 1  # 사전이니까 append x
#                     # maxCnt[num] = 1 할필요가 없다.최소 두번나와야 코스요리 가능이라서.
#                 else:
#                     foodMap[num][key] += 1
#                     maxCnt[num] = max(maxCnt[num], foodMap[num][key])

#     for num in course:
#         for key, value in foodMap[num].items():
#             # value가 2이상이고, maxCnt와 같으면 answer에 추가
#             if value >= 2 and value == maxCnt[num]:
#                 answer.append(key)

#     return sorted(answer)

import collections

# from collections import defaultdict
import itertools


def solution(orders, course):
    result = []
    # d, m = defaultdict(int), defaultdict(lambda: 2)
    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return ["".join(v) for v in sorted(result)]


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
