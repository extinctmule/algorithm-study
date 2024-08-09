'''
완전탐색 가능한가?
10!=24*30*56*90= 720*4940 = 대충 494000 가능?
'''
def check(a,brk):
    for i in range(len(a)-1):
        if brk[i]=='<':
            if a[i]>=a[i+1]:
                return False
        else:
            if a[i]<=a[i+1]:
                return False

from itertools import permutations
import sys

input = sys.stdin.readline

k = int(input())
brk = list(input().split())

zeroten = [i for i in range(0,10)]

arr = permutations(zeroten, k+1)
ans = []

for a in arr:
    if check(a,brk):
        ans.append("".join(map(str,a)))

print(max(ans))
print(min(ans))