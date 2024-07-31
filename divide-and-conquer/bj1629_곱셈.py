'''
(A*A)%C == (A%C * A%C)%C
'''

def go(A,B,C):
    if B==1:
        return A
    
    cur = go(A,B//2,C)
    
    # B//2 번 만큼의 계산이 끝났다는 뜻이므로,
    if B%2:
        return (((cur %C)**2)%C * A)%C
    else:
        return ((cur %C)**2)%C

A, B, C = map(int,input().split())

print(go(A,B,C))