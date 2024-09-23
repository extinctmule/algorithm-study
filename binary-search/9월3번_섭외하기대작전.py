"""
1 2 5 99
"""

import bisect

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
# 3 5 6 7 7
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = bisect.bisect_right(arr, arr[i] + arr[j])
        ans += k - (j + 1)

print(ans)
