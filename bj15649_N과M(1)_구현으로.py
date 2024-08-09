'''
엣지케이스 따로없는듯?
순열로
'''

import sys
from itertools import permutations

input = sys.stdin.readline

N,M = map(int, input().split())

p = permutations(range(1,N+1),M)

for lst in p:
    for l in lst:
        print(l,end=' ')
    print()