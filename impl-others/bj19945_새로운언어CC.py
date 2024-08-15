def half(num):
    if num < 2:
        return 1

    return half(num // 2) + 1


n = int(input())
if n < 0:
    print(32)
else:
    print(half(n))
