# 5:55~6:17
# 다솜이는 마스터가되기위해 도감완성시켜야함.
# 현재의 포켓몬 도감에서 이름보면 번호 또는 번호보면 이름 말하는 연습해야함.
# 포켓몬개수 N, 문제의개수M
# 1<= N, M <= 100,000

# 포켓몬이름은 첫글자 대문자 나머지 소문자, 근데 일부 포켓몬은 마지막만 대문자<- 이거 abcN 이라는 소리 맞음?;;<-안중요?
# 길이는 2~20
# 입력으로 들어오는 숫자는 1<=입력 <= N

N, M = map(int, input().split())
d = {}
for i in range(1,N+1):
    pok = input()
    d[pok]=i
    d[str(i)] = pok

pro = [input() for _ in range(M)]

ans = []

for p in pro:
    print(d[p])