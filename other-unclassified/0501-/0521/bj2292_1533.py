import math

N = int(input())

# N = 6*0 + 6*1 + 6*2 + ... + 6*(i)
# N = 6*(i*(i+1)/2) 근의공식 풀면,
if N == 1:
    print(1)
else:
    res = 2 + ((-3 + math.sqrt(9 + 12 * (N - 2))) // 6)
    print(int(res))
