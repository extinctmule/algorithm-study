
N = int(input())

ans =0
for _ in range(N):
    word = list(input())
    s = []
    for w in word:
        if s and w==s[-1]:
            s.pop()
        else:
            s.append(w)

    if not s:
        ans+=1
print(ans)