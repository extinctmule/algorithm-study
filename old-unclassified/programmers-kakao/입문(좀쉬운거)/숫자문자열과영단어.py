from collections import deque
from io import StringIO


def solution(s):
    # res = deque()#deque로 했을때 평균 0.03ms
    res = ""  # 0.02ms임
    # 버퍼사용해도 안빨라졌음
    alpha = list("abcdefghijklmnopqrstuvwxyz")

    i = 0
    while True:
        try:
            if s[i].isdigit():
                res += s[i]
                i += 1
            elif s[i] == "z":
                res += "0"
                i += 4
            elif s[i] == "o":
                res += "1"
                i += 3
            elif s[i] == "t":
                if s[i + 1] == "w":
                    res += "2"
                    i += 3
                else:  # 'h'
                    res += "3"
                    i += 5
            elif s[i] == "f":
                if s[i + 1] == "o":
                    res += "4"
                    i += 4
                else:  #'i'
                    res += "5"
                    i += 4
            elif s[i] == "s":
                if s[i + 1] == "i":
                    res += "6"
                    i += 3
                else:
                    res += "7"
                    i += 5
            elif s[i] == "e":
                res += "8"
                i += 5
            else:  # nine
                res += "9"
                i += 4

        except:
            break

    return int(res)


print(solution("1"))
