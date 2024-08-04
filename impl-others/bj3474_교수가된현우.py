'''
잘 모르겠다..
2,5 나 4,5 나 6,5 암튼 5를 넘기면 하나 생기고10에서 하나 더 생기고
5! 120
10! ..800
12! ..600
15! ..8000
20! ..40000

-> 답보고 품
5의 배수의 개수를 구하면 되는 문제. 이유: 2*5긴 한데,
2는 걍 2,4,6,8, .. 다 산재해있어서 신경x

'''

import sys
input = sys.stdin.readline
T = int(input())
arr = [int(input()) for _ in range(T)]
ans =[]
for num in arr:
    zeros = 0
    baesu = 5
    while baesu <= num:
        zeros += num//baesu
        baesu*=5
    ans.append(zeros)

print('\n'.join(map(str,ans)))