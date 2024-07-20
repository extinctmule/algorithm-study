T = int(input())

for i in range(1, T + 1):

    s = input()
    N = len(s)
    pal1 = (N - 1) // 2

    if s[:pal1] == s[:pal1:-1]:
        s2 = s[:pal1]
        pal2 = pal1 // 2

        if s2[:pal2] == s2[-1 : -pal2 - 1 : -1]:
            print(f"#{i} YES")
            continue

    print(f"#{i} NO")
