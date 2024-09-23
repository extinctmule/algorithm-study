"""
N! 를 소인수분해해서 그안에 5가 몇번 나오는지
5 = 5*1
10 = 5*2
15 = 5*3
20 = 5*4
25 = 5*5
30 = 5*6
근데
50 = 5*5*2
하지만 어차피
5*5*3
5*5*4
를 통해
125 = 5*5*5
까지 가는거니까..

예를들어 10! 은 5*(1+1)
35! = 5*(7)+5*(5*1)이므로
125!는 결국
(1+...)

5의 제곱수의 제곱을 더해가고, 그수가 N보다 크면 중단

즉 답은 N//5 + N//5*5 + ...
"""

N = int(input())

i = 5
res = 0

while i <= N:
    res += N // i
    i *= 5

print(res)
