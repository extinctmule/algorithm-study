#11:30~12:06
# 입력 N 범위: 1~150

#alpha 26크기 리스트 만들어서 sort 한 뒤 세면 편할것같은데..

N = int(input())
lst = [input() for _ in range(N)]
lst.sort()

lstset = set()

for s in lst:
    lstset.add(s[0])

firsts = list(lstset)
firsts.sort()

firsts_dict = {k:0 for k in firsts}

for s in lst:
    firsts_dict[s[0]]+=1

ans = []
for k,v in firsts_dict.items():
    if v>=5:
        ans.append(k)

if ans:
    print("".join(ans))
else:
    print("PREDAJA")