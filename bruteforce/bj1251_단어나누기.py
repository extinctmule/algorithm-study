"""
for루프 1~len-2, 그안에서 i+1 ~ len-1 다시 돌리고
그안에서 매번 작은거비교해서 저장
"""

word = input()
ans = word[:2] + word[2:][::-1]

for i in range(1, len(word) - 2):
    first = word[:i][::-1]
    for j in range(i, len(word) - 1):
        ans = min(ans, first + word[i : j + 1][::-1] + word[j + 1 :][::-1])

print(ans)
