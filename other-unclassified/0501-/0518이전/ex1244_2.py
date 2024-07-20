def dfs(n):
    global ans, L
    if n == N:
        ans = max(ans, int("".join(S)))
        return
    for i in range(L - 1):
        for j in range(i + 1, L):
            S[i], S[j] = S[j], S[i]
            chk = int("".join(S))
            if (n, chk) not in v:
                dfs(n + 1)
                v.append((n, chk))
            S[i], S[j] = S[j], S[i]


T = int(input())

for tc in range(1, T + 1):
    S, N = map(int, input().split())
    S = list(str(S))
    L = len(S)
    ans = 0
    v = []
    dfs(0)
    print("#{} {}".format(tc, ans))

# n = int(input())


# def dfs(num, cnt, depth):
#     if cnt == 0:
#         answer.append(num)
#         return
#     if depth == len(num):
#         if cnt % 2 == 0:
#             answer.append(num)
#         elif len(set(num)) != len(num):
#             answer.append(num)
#         else:
#             answer.append(num[:-2] + num[-1] + num[-2])
#         return
#     for idx in range(depth, len(num)):
#         if num[idx] == max(num[depth:]):
#             if num[depth] != num[idx]:
#                 dfs(
#                     num[:depth]
#                     + num[idx]
#                     + num[depth + 1 : idx]
#                     + num[depth]
#                     + num[idx + 1 :],
#                     cnt - 1,
#                     depth + 1,
#                 )
#             else:
#                 dfs(num, cnt, depth + 1)


# for case in range(1, n + 1):
#     data, r = input().split()
#     r = int(r)
#     answer = []
#     dfs(data, r, 0)
#     print(f"#{case} {max(answer)}")
