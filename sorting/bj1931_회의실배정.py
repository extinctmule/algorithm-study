"""
각 회의 I에대해 시작시간, 종료시간.
회의 사용할 수 있는 최대 개수 찾아보자.
이전회의 종료시간 = 다음회의 시작시간 가능
한 회의의 시작시간 = 종료시간 가능

N은 100,000이므로 시간복잡도 NlogN 정도까지가능?
시작시간범위 0~2^31 -1.. 인접행렬같은거 쓰기힘들듯

종료시간 제일작은숫자 회의(들)찾고,
그중에서 시작시간>= 이전회의종료시간 있으면 진행하고,
없으면 그다음으로 종료시간 작은거~

"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))

ans = 1
end = arr[0][1]

for i in range(1, N):
    if end <= arr[i][0]:
        ans += 1
        end = arr[i][1]

print(ans)
