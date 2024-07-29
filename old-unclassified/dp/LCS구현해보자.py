# 일단.. 재귀로 풀수가있었다
# 아 근데 재귀로 푸는 방식도 결국 DP를 이용하는건가?
def lcs(A, B, i, j):
    if i <= 0 or j <= 0:
        return ""

    # 같으면 그 lcs(A,B,i-1,j-1)+A[i]
    if A[i] == B[j]:
        return lcs(A, B, i - 1, j - 1) + A[i]

    # 다를시 하나는 i-1, 다른하나는 j-1 하고나서
    else:
        s1 = lcs(A, B, i - 1, j)
        s2 = lcs(A, B, i, j - 1)

        return s1 if len(s1) >= len(s2) else s2


A = "ABDBCA"
B = "CBBADDCABBA"

asize, bsize = len(A), len(B)

res = lcs(A, B, asize - 1, bsize - 1)  # 인덱스편하게쓰기위해 마지막문자부터 ㄱㄱ
print(res)
