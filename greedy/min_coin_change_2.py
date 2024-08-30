# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
import sys


def minCoins(coins, m, sum):
    table = [sys.maxsize for _ in range(sum + 1)]

    table[0] = 0

    for i in range(1, sum + 1):
        for j in range(m):
            if i - coins[j] >= 0:
                sub_res = table[i - coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1

    if table[sum] == sys.maxsize:
        return -1

    return table[sum]


if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    m = len(coins)
    sum = 11
    print(minCoins(coins, m, sum))
