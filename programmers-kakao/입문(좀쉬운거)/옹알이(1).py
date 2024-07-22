def solution(babbling):
    answer = 0
    # 중요: babbling에서 저 네가지는 각각 최대 한번씩만.
    for s in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            if w in s:
                s = s.replace(w, " ")

        if not s.strip():
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
