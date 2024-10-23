"""
수학을 이용해서 최적화를 해야 하는 시뮬레이션 문제.
적 N명
데미지: 1 2 3 4 1 2 3 4
1 1
3 2 3
2 4
4 1 2 3

"""

import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
ans = 0

j = 0
fours = [[1, 3, 6, 10], [2, 5, 9, 10], [3, 7, 8, 10], [4, 5, 7, 10]]

for i in range(1, N + 1):
    tmp = 0
    hp = arr[i]

    if hp <= fours[j][0]:
        tmp += 1
    elif hp <= fours[j][1]:
        tmp += 2
    elif hp <= fours[j][2]:
        tmp += 3
    elif hp < 10:
        tmp += 4

    tmp += 4 * (hp // 10)

    ans += tmp
    j += tmp
    j %= 4

print(ans)
