from collections import deque
from io import StringIO


def solution(s):
    # res = deque()#deque로 했을때 평균 0.03ms
    # res = ""  # 이것도 걍 0.03ms임
    alpha = list("abcdefghijklmnopqrstuvwxyz")

    buffer = StringIO()
    i = 0
    while True:
        try:
            if s[i].isdigit():
                buffer.write(s[i])
                i += 1
            elif s[i] == "z":
                buffer.write("0")
                i += 4
            elif s[i] == "o":
                buffer.write("1")
                i += 3
            elif s[i] == "t":
                if s[i + 1] == "w":
                    buffer.write("2")
                    i += 3
                else:  # 'h'
                    buffer.write("3")
                    i += 5
            elif s[i] == "f":
                if s[i + 1] == "o":
                    buffer.write("4")
                    i += 4
                else:  #'i'
                    buffer.write("5")
                    i += 4
            elif s[i] == "s":
                if s[i + 1] == "i":
                    buffer.write("6")
                    i += 3
                else:
                    buffer.write("7")
                    i += 5
            elif s[i] == "e":
                buffer.write("8")
                i += 5
            else:  # nine
                buffer.write("9")
                i += 4

        except:
            break

    return int(buffer.getvalue())


print(solution("1"))
