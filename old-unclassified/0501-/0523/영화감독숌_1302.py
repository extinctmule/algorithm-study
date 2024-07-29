N = int(input())

doom = 665

for cur in range(1, N + 1):
    while True:
        doom += 1
        if "666" in str(doom):
            break

print(doom)
