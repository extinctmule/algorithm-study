'''
4:10~
빈도를 조사하여 암호를 해킹할 수 있다.
메시지: 숫자 N개로 이루어진 수열, 숫자<=C (C값 주어지는게 의미가 있나?)
이를 자주 등장하는 빈도순대로 내림차순 정렬.
등장횟수 같다면, 먼저 나온 것이 앞에있어야 함.
그냥 counter 사용?
1<=N<=1000 이므로 리스트 범위 내.
'''
from collections import Counter

N, C = map(int, input().split())
arr = list(map(int, input().split()))

cnt = Counter(arr)

i = 0
ans = []
for k,v in cnt.most_common():
    ans.extend([k]*v)
    
print(" ".join(map(str, ans)))
    