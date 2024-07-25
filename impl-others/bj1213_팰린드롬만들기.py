# 9:30~10:37
# 영어이름의 알파벳순서를 적절히 바꿔서 팰린드롬을 만들자.
# 입력: 최대 50글자
# 정답 여러개일 경우 사전순으로 앞서는 것을 제시. 
# 불가능할 시, "I'm Sorry Hansoo" 출력


# 먼저 사전순 정렬 해놓고 시작하자.

# 문자열길이 홀수일 경우, 아마 알파벳 중 하나만 홀수개일 수 있다.
# 실수: 중간에오는 알파벳뭉치ACCCA 이런식으로 구현하면안되고, AAABB에대해 BAAAB가 아닌, ABABA로 해야함.
# 여러개가 홀수개이면 불가능
# 문자열길이 짝수일 경우, 어떤 알파벳도 홀수개일 수 없다.
def sol(sdict, odds):
    ans = []
    olen = len(odds)
    if olen<=1:
        ch = ''
        if olen==1:
            ch = list(odds)[0]
            
        for k, v in sdict.items():
            for _ in range(v//2):
                ans.append(k)

        return ''.join(ans)+ch+''.join(ans[::-1])

    else:
        return "I'm Sorry Hansoo"

s = input().strip()
n = len(s)

s = ''.join(sorted(s))
sdict = {k:0 for k in s}

for ch in s:
    sdict[ch]+=1
    
if len(sdict)==1:
    print(s)
else:
    odds ={}
    for k,v in sdict.items():
        if v%2==1:
            odds[k]=v
    
    print(sol(sdict, odds))

'''
ABCD


'''