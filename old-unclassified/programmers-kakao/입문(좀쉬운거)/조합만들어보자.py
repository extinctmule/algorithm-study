order = "ABCD"

n = len(order)

table = [[] for _ in range(n + 1)]

for i in range(n):
    table[0].append(order[i])

# for i in range(1, n):
#     for j, item in enumerate(table[i - 1]):
#         for k in range(j+1, n):
#             table[i].append(item + order[k])

# Generate combinations
for i in range(1, n):
    for item in table[i - 1]:
        start_index = order.index(item[-1]) + 1
        for k in range(start_index, n):
            table[i].append(item + order[k])

print(table)
