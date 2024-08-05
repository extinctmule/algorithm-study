'''
6:01~8:20?
경기시간: 48분
팀번호는 1과 2
00:00~ 47:59

비기고있던 시간은 빼고,
현재상태 score: 0(비기는중), -(1팀이기는중), +(2팀이기는중) 로 구분
아이거 그냥 초로 바꿔풀자
'''
goals = int(input())
team1, team2 = 0, 0
dct = {'1':-1, '2':1}

stamps = []#점수, 시간

for i in range(goals):
    team, clock = input().split()
    m,s = map(int, clock.split(':'))
    
    stamps.append([dct[team], m*60+s])
    if i>0:
        stamps[i][0]+=stamps[i-1][0]

stamps.append([stamps[-1][0],48*60])#경기종료시점

for i in range(1,goals+1):
    if stamps[i-1][0]<0:
        team1+= stamps[i][1]-stamps[i-1][1]
    elif stamps[i-1][0]>0:
        team2+= stamps[i][1]-stamps[i-1][1]

print(f'{team1//60:02d}:{team1%60:02d}\n{team2//60:02d}:{team2%60:02d}')
