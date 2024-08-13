"""
깊이가 K인 이진트리는 총 2^K-1개의 노드로 이뤄짐
왼 현 우 순회
한 걸 레벨별로 번호 출력.

"""

K = int(input())
arr = list(map(int, input().split()))
ans = []
l = 2**K - 1

for i in range(0, K):
    ans.append([])
    for j in range(2**i - 1, l, 2 ** (i + 1)):
        ans[i].append(arr[j])

for i in range(K - 1, -1, -1):
    print(" ".join(map(str, ans[i])))
