'''
다트 세차례 던지기
점수: 0~10
영역: S, D면 2제곱, T면 3제곱
옵션:
*면 직전에 얻은 점수들 각각 *2(처음에나왔으면 그것만*2), 2번*나오면 중첩가능 
#면 '해당점수만' 마이너스
테케 주의: 점수 10
'''

def solution(dr):
    scores = [[1]*3 for _ in range(3)]
    bonus = {'S':1,'D':2,'T':3}
    options={'*':2,'#':-1}
    # 입력값 나누는것부터 시작해보자.
    cur =0
    for n in range(3): # 여기의 scores[n][0]<- 0,1,2하드코딩해야하는데 i로 놓는 실수함. 인덱스변수 너무 정신없어서 개선해야함
        i=0
        if dr[cur+i]=='1' and dr[cur+i+1]=='0':
            scores[n][0]=10
            i+=2
        else:
            scores[n][0]=int(dr[cur+i])
            i+=1

        scores[n][1] = bonus[dr[cur+i]]
        i+=1
        
        if cur+i<len(dr):
            if dr[cur+i] in ['*','#']:#옵션 존재할경우
                scores[n][2] = options[dr[cur+i]]
                i+=1
            else:
                scores[n][2] = 1
        cur += i
        
    lst = [0]*3
    for i in range(3):
        lst[i] = scores[i][0]**scores[i][1]*scores[i][2]
        
        if scores[i][2]==2 and 1<=i<=2:
            lst[i-1] *= 2 # 직전꺼 적용
    
    return sum(lst)

'''
1S2D*3T
1D2S#10S
1D2S0T
1S*2T*3S
1D#2S*3S
1T2D3D#
1D2S3T*
print(solution('1S#2T*3T*'))
'''

