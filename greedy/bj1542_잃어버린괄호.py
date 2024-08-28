"""
입력받은것
스택으로 넣다가 +,- 만나면 배열에추가

앞부분 +는 무시하고 
-만나면 뒷부분에서 다시 -만날때까지 다 합쳐서 빼기
"""

eq = input()
arr = eq.split("-")

ans = sum(list(map(int, arr[0].split("+"))))
for i in range(1, len(arr)):
    ans -= sum(list(map(int, arr[i].split("+"))))

print(ans)


# tmp = input()

# arr = []
# stack = []

# for c in tmp:
#     if c != "+" and c != "-":
#         stack.append(c)
#     else:
#         arr.append(int("".join(stack)))
#         arr.append(c)
#         stack = []
# arr.append(int("".join(stack)))

# i, n = 0, len(arr)
# ans = 0

# while i < n:
#     if arr[i] != "+" and arr[i] != "-":
#         ans += arr[i]
#     elif arr[i] == "-":
#         i += 1
#         while i < n:
#             if arr[i] != "-" and arr[i] != "+":
#                 ans -= arr[i]
#             elif arr[i] == "-":
#                 i -= 1
#                 break
#             i += 1
#     i += 1

# print(ans)
