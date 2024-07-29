# list로 변환해서 풀어보고 시간비교
#   ->str이 더 빨랐다. 시간 1/4정도
def mysol(nid: str):
    nid = nid.lower()
    nid1 = list(nid)

    # 2
    nid2 = []
    for c in nid1:
        if c not in "~!@#$%^&*()=+[{]}:?,<>/":
            nid2.append(c)
    # 3

    i = 1
    while True:
        if i >= len(nid2):
            break
        if nid2[i - 1] == "." and nid2[i] == ".":
            nid2.pop(i)
        else:
            i += 1
    # 4
    try:
        if nid2[0] == ".":
            nid2.pop(0)
        if nid2[-1] == ".":
            nid2.pop()
    except:  # 5 빈 문자열
        nid2.append("a")

    # 6
    if len(nid2) >= 16:
        nid2 = nid2[:15]
        while nid2[-1] == ".":
            nid2.pop()
    # 7
    for _ in range(len(nid2), 3):
        nid2.append(nid2[-1])

    return "".join(map(str, nid2))


def solution(new_id: str):
    answer = mysol(new_id)
    return answer


print(solution("=.="))
