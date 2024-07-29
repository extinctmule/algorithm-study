A, B, C = map(int, input().split())

cur = A
ac = A%C

for _ in range(B-1):
    cur = ((cur%C) * ac)%C
print(cur)