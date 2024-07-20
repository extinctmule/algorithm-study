# Bottom-up
# def fibo_bu(N):

#     for i in range(2, N + 1):
#         arr[i] = arr[i - 2] + arr[i - 1]


# Top-down
def fibo_td(N):

    if arr[N - 1] == -1:
        fibo_td(N - 1)
    arr[N] = arr[N - 2] + arr[N - 1]


N = int(input())
arr = [-1 for _ in range(N + 1)]
arr[0], arr[1] = 0, 1

fibo_td(N)
print(arr)
