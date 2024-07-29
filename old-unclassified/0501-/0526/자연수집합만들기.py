# def P(n, k):
#     if k == 1:
#         return [n]
#     if n == k:
#         return [1 for _ in range(n)]
#     #if n<k:#error


# def num_cases(n, cur, res):
#     if n == 0:
#         return []
#     if n == 1:
#         return [1]
#     for i in range(1, n):
#         cur = [i] + num_cases(n - i, [], res)
#         res.append(cur)

#     return cur


# res = []
# cur = []
# cases = num_cases(4, cur, res)

# print("cur", cur)
# print("res", res)

# def num_cases(n, res):
#     if n == 1:
#         return [1]
#     for i in range(1, n):
#         res.append([i] + num_cases(n - i))
