# 12:10~
# 서버망가져서 특정패턴과 일치하는 파일 이름을 적절히 출력못하는 상황
# 패턴: 알파벳소문자 여러개와 별표 하나로 이루어진 문자열
# 패턴에 있는 * 를 알파벳소문자로 이루어진 임의의 문자열로 변환필요
# 별표는 "" 즉 빈 문자열로 바꿀 수도 있다
# 별표는 문자열의 시작이나 끝에 있지 않다.

# 파일개수 N: 1~100, 문자열길이 및 파일이름길이:100이하

N = int(input())
pat = input()
P = len(pat)

files = [input() for _ in range(N)]

# for i in range(P):
#     if pat[i]!='*':
#         cut+=1
#     else:
#         break
cut = pat.index('*')

fpat = pat[:cut]
bpat = pat[cut+1:]

flen, blen = len(fpat), len(bpat)

for s in files:
    slen = len(s)
    if slen < flen + blen:# *이 공백으로 대체돼도 된다그랬으니까 ==까지 됨
        print("NE")
    elif s[:cut]== fpat and s[slen-blen:slen]==bpat:
        print("DA")
    else:
        print("NE")


'''
4
a*addd
addddd
addd
fik
fiejiffejfei
'''