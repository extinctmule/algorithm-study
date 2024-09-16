"""
앞부분: 일단 길이-2까지중에 제일 작은알파벳에서 끊기(같을경우 더 앞)
중간: 거기서부터 길이-1까지중에 제일 작은거
뒷부분:ㅇㅇ
"""

s = input()
slen = len(s)
ans = []

for i in range(1, slen - 1):
    for j in range(i + 1, slen):
        first = s[:i]
        second = s[i:j]
        third = s[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        ans.append("".join(first + second + third))

print(min(ans))
