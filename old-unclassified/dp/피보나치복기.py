# fibo dp

# input
N = 12

fibo = [None] * N

fibo[0] = 0
fibo[1] = 1

for i in range(2, N):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo)
