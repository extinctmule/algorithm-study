import sys
sys.stdin = open("input05191329.txt", "r")

ab = ['a', 'b']
T = int(input())

def solve(s, n):

    for i in range(n):
        
        if s[i] in ab:
            for j in range(i,n):
                if s[j] not in ab:
                    print(s[j+1:], n-j-1)
                    return i+2 + solve(s[j+1:], n-j-1)
            else:
                return i+1
    return n


for tc in range(1,T+1):
    N = int(input())
    S = input()

    ans = solve(S,N)

    print(f"#{tc} {N - ans}")