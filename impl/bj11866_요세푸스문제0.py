# 9:59~10:35
# 원으로 1~N
# 1~N 사이의 수 K 주어짐.

# N의 범위는 1000. O(N^2)넘어가면 안됨
N, K = map(int, input().split())
lst = [i for i in range(1,N+1)]
ans = []

cur = K-1# 와 이걸 2라고 적어두는 실수함.

for i in range(N-1):# zerodivision 피하기위해 마지막꺼 따로.
    ans.append(lst[cur])
    lst.remove(lst[cur])
    cur = (cur + K-1)%(N-i-1)

ans.append(lst[0])# 마지막꺼

print('<'+", ".join(map(str, ans))+'>')


'''
import sys
from collections import deque

ans_list = []
N, K = map(int,sys.stdin.readline().split())

table = deque([i+1 for i in range(N)])
while(table):
    table.rotate(-(K - 1))
    ans_list.append(table.popleft())
ans = ', '.join(map(str,ans_list))
print(f'<{ans}>')
'''