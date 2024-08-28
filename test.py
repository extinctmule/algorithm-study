eq = input()
arr = eq.split("-")

ans = sum(list(map(int, arr[0].split("+"))))
for i in range(1, len(arr)):
    ans -= sum(list(map(int, arr[i].split("+"))))

print(ans)
