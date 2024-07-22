fees = [0]*4# 인덱스 1부터 사용한다.
fees[1], fees[2], fees[3] = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(3)]

# 하나는 입장시간으로 오름차순
times.sort(key=lambda x: x[0])

# 아 수학개념으로 구현하려 하지말고 입력값 작으니까 그냥 크기100 리스트 만들자
car0, car1, car2 = [0]*101, [0]*101, [0]*101

# car0[times[0][0]:times[0][1]] = 1 # 틀림
car0[times[0][0]:times[0][1]] = [1] * (times[0][1] - times[0][0]) # 맞음
car1[times[1][0]:times[1][1]] = [1] * (times[1][1] - times[1][0])
car2[times[2][0]:times[2][1]] = [1] * (times[2][1] - times[2][0])

start, end = times[0][0], max(times[0][1],times[1][1],times[2][1])

ans = 0

for i in range(start, end):
    num = car0[i]+car1[i]+car2[i]
    ans += num*fees[num]

print(ans)

'''
5 3 1
1 6
2 8
3 5

1~2: 1
3~5: 2*5*3
4*3*2+

100 10 1
1 6
2 8
3 5

100 10 1
1 2
3 4
5 6


'''

