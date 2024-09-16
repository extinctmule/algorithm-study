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
