"""
*서로다른* 양의 정수
수열의크기 1<= n <=100,000

투포인터 문제
시간내에 못풀고 답보고 품
"""

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

ans = 0
# 1 2 3 5 7 9 10 11 12

left, right = 0, n - 1

# 현재값에 따라 투포인터 가운데 향해 움직이면 됨,
# 더이상 포인터를 가운데로 움직일 수 없으면 종료
while left < right:
    tmp = arr[left] + arr[right]
    if tmp < x:
        left += 1
    elif tmp > x:
        right -= 1
    else:
        ans += 1
        left += 1

print(ans)
