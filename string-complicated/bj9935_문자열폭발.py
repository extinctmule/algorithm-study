"""
폭발: 모든 폭발문자열이 폭발. 남은 거 순서대로 이어붙이게 됨.
새로 생긴문자열도 다시 체크, 없을때까지 계속.

폭발문자열 안에는 같은문자가 없음

빈문자열이 될경우 "FRULA" 출력
abc
aabcbc
ababcc
"""

import sys

input = sys.stdin.readline

s = list(input().strip())
pat = list(input().strip())
plast = pat[-1]

slen, plen = len(s), len(pat)
ans = []

i, n = 0, slen

for c in s:
    ans.append(c)

    if c == plast and i >= plen - 1:
        if ans[-plen:] == pat:
            del ans[i - plen + 1 : i + 1]
            n -= plen
            i -= plen
    i += 1

if ans:
    print("".join(ans))
else:
    print("FRULA")
