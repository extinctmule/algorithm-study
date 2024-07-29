def hexToBi(str1, str2):
    
    
    
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    clist = []
    
    for _ in range(0,N):
        s = input()

        start,k, end = 0,0,0
        width =0
        while k<M:
        for i in range(end, M):
            if s[i]!='0':
                start = i
                break
        if start!=0:
            for i in range(start+1, M):
                if s[i]=='0':
                    end = i#주의: 마지막인덱스 + 1 
                    break
        
        sl = end-start
        
        if start==end:
            continue
        
        c = s[start:end]
        
        if c not in clist:
            clist.append(c)#가짜코드든 진짜든 간에 일단 저장
        