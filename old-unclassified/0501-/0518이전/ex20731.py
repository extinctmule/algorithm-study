# def coprime(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a == 1


# str100 = ["?"] * 52
# str52mat = [str52] * 52

# for i in range(52):
#     # str52 = ["?"] * 52
#     for j in range(i, 52):
#         # j가 i보다 항상크거나같으므로 순서 바꿔서 넣는게 coprime루프 줄일듯
#         if coprime(j, i):
#             str52mat[i][j] = "1"
#             str52mat[j][i] = "1"
#     # str52list.append("".join(str52))

# str52list = []

# for i in range(52):
#     str52list.append("".join(str52mat[i]))

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())

#     strlist = [input() for _ in range(N)]

#     if strlist == str52list[:N]:
#         print(f"#{tc} YES")
#     elif strlist == str52list[1 : N + 1]:
#         print(f"#{tc} YES")
#     elif strlist == str52list[2 : N + 2]:
#         print(f"#{tc} YES")
#     else:
#         print(f"#{tc} NO")
