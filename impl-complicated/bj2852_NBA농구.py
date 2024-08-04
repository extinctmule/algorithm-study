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
#stamps = [0,0]#초기

for i in range(goals):
    team, clock = input().split()
    s = int(clock[0]+clock[1])*60+int(clock[3]+clock[4])
    if stamps:
        stamps.append([dct[team]+stamps[-1][0], s])
    else:
        stamps.append([dct[team], s])
    

stamps.append([stamps[-1][0],48*60])#경기종료시점

for i in range(1,goals+1):
    if stamps[i-1][0]<0:
        team1+= stamps[i][1]-stamps[i-1][1]

    elif stamps[i-1][0]>0:
        team2+= stamps[i][1]-stamps[i-1][1]

def int_to_str(num):
    m = str(num//60)
    s = str(num%60)
    if len(m)==1:
        m = '0'+m
    if len(s)==1:
        s='0'+s
    return m+':'+s

print(int_to_str(team1))
print(int_to_str(team2))