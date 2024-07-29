alpha = dict()

s = input()
s = s.lower()

for c in s:
    alpha[c] = 0
for c in s:
    alpha[c] += 1

most_used = max(alpha.values())
res = [k for k, v in alpha.items() if v == most_used]

if len(res) > 1:
    print("?")
else:
    print(res[0].upper())  # upper()해주기
