T = int(input())

for i in range(1, T + 1):
    A, B = input().split()
    if A == B:
        print(f"#{i} {A}")
    else:
        print(f"#{i} 1")
