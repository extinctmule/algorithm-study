# abcdefghijklm / nopqrstuvwxyz
S = input()
ans = []

for i, c in enumerate(S):
    if 'a'<=c<='m' or 'A'<=c<='M':
        ans.append(chr(ord(c)+13))
    elif 'n'<=c<='z' or 'N'<=c<='Z':
        ans.append(chr(ord(c)-13))
    
    else:
        ans.append(c)

print("".join(ans))