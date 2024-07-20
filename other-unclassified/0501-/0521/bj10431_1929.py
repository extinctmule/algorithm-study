import sys

input = sys.stdin.readline
P = int(input())

for tc in range(1, P + 1):
    hlist = list(map(int, input().split()))
    hlist.remove(hlist[0])

    lines = [hlist[0]]  # 인덱스 0부터임.
    steps = 0

    for i in range(1, 20):
        # lines.append(hlist[i])#가정.연산줄이기위해 마지막에 처리

        for j in range(0, i):
            if lines[j] > hlist[i]:
                temp = lines[:j]
                temp.append(hlist[i])
                lines = temp + lines[j:]
                steps += i - j
                break
        else:
            lines.append(hlist[i])

    print(tc, steps)


"""
1
2 919 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900

"""
