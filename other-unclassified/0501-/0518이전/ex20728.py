def merge(bags, lo, mid, hi):
    if bags[mid] <= bags[mid + 1]:
        return

    i = lo
    j = mid + 1
    aux = bags[lo : hi + 1]

    for k in range(lo, hi + 1):
        if i > mid:
            bags[k] = aux[j - lo]
            j += 1
        elif j > hi:
            bags[k] = aux[i - lo]
            i += 1
        elif aux[i - lo] <= aux[j - lo]:
            bags[k] = aux[i - lo]
            i += 1
        else:
            bags[k] = aux[j - lo]
            j += 1


def binarySort(bags, lo, hi):
    if lo < hi:
        mid = lo + (hi - lo) // 2  # 파이썬이다. /가 아니라 //로 해야함.

        binarySort(bags, lo, mid)
        binarySort(bags, mid + 1, hi)
        merge(bags, lo, mid, hi)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
sol = [None] * (T + 1)
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # map부분 빼먹으면 안됨.
    bags = list(map(int, input().split()))

    binarySort(bags, 0, N - 1)  # N 맞나?

    res = bags[K - 1] - bags[0]

    for i in range(1, N - K + 1):
        res = min((bags[i + K - 1] - bags[i]), res)

    sol[test_case] = res

for test_case in range(1, T + 1):
    print(f"#{test_case} {sol[test_case]}")
