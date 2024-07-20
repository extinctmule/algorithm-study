T = int(input())

ns = []
for i in range(T):
    ns.append(int(input()))

m = max(ns)

arr = [0 for _ in range(m + 1)]
arr[1], arr[2], arr[3] = 1, 2, 4

# dp만들기
for i in range(4, m + 1):
    arr[i] = sum(arr[i - 3 : i])

# 정답 출력
for n in ns:
    print(arr[n])
