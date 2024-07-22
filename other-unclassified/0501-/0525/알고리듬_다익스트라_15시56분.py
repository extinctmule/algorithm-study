import math


def dij(si):
    d[si] = 0
    pq = [si]

    while pq:
        tmp = min([d[i] for i in pq])
        ci = d.index(tmp)
        pq.pop(pq.index(ci))  # q.pop(ci) 이러면 안됨. 인덱스를 다시찾아서 해야함

        for ni in range(N):
            # -1체크는 이어진간선인지 체크하는것임.
            # d[ni]값 비교하는 부분, min으로 했다가 무한루프됨.
            # 이거 먼저 체크하고 그후에 pq안에 ni가 있는지 그때 확인해야함.
            if arr[ci][ni] != -1 and d[ni] > d[ci] + arr[ci][ni]:
                d[ni] = d[ci] + arr[ci][ni]

                if ni not in pq:
                    pq.append(ni)
        print("q:", pq)


N = int(input())
pairs = int(input())
arr = [[-1 for _ in range(N)] for _ in range(N)]
d = [math.inf for _ in range(N)]  # 시작위치만 0으로 만들어주자.

for _ in range(pairs):
    a, b, val = map(int, input().split())
    arr[a][b] = val

dij(0)

"""
5
10
0 1 10
0 3 5
1 2 1
1 3 2
2 4 4
3 1 3
3 2 9
3 4 2
4 0 7
4 2 6

"""
