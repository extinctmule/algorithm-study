import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    nlist, times = input().split()
    nlen = len(nlist)

    nlist = [int(c) for c in nlist]
    times = int(times)

    ideal = sorted(nlist, reverse=True)

    count = times

    for i in range(nlen):

        if count <= 0:
            break
        if ideal == nlist:
            if count % 2:  # 예외 추가해야함!!
                if len(nlist) == len(set(nlist)):
                    # 중복값 없는 ideal이라면,어쩔 수 없이
                    nlist[-1], nlist[-2] = nlist[-2], nlist[-1]
            break

        for j in range(i, nlen):
            target = ideal[j]

            if nlist[j] != target:

                # k = nlist[::-1].index(target)  # 역순으로, 원하는것 찾음
                indices = [i for i, x in enumerate(nlist) if x == target]
                k = indices[-1]

                if len(indices) > 1:
                    supposedtobe = ideal.index(nlist[j])
                    if supposedtobe in indices:
                        k = supposedtobe

                # nlist[nlen-k-1]대신 nlist[-k-1] 이거 가능
                nlist[j], nlist[k] = nlist[k], nlist[j]
                count -= 1
                break

    print(f"#{tc} {''.join(map(str,nlist))}")


"""
t=int(input())
 
result=0
visited=[]
def dfs(depth):
    global result
    if depth==n:
        result = max(result, int("".join(array)))
        return
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            array[i], array[j] = array[j], array[i]
            if [depth+1, "".join(array)] in visited:
                array[i], array[j] = array[j], array[i]
                continue
            visited.append([depth+1, "".join(array)])
            dfs(depth+1)
            array[i], array[j] = array[j], array[i]
 
for num in range(1, t+1):
     
    result=0
    visited=[]
    array, n=map(str, input().split())
    n=int(n)
    array=[a for a in array]
     
    dfs(0)
 
 
     
    print("#", end="")
    print(num, end=" ")
    print(result)
"""
