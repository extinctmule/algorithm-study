H, W, N, M = map(int, input().split())

print(((W - 1) // (M + 1) + 1) * ((H - 1) // (N + 1) + 1))
