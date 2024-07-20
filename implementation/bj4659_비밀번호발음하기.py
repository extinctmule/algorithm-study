vowel = ("a", "e", "i", "o", "u")

while True:
    pw = input()

    if pw == "end":
        break

    # 모음 적어도 하나
    for v in vowel:
        if v in pw:
            break
    else:
        print(f"<{pw}> is not acceptable.")
        continue

    # 모음 혹은 자음이 3개연속 오면 안됨
    pw_01 = []
    for i in range(len(pw)):
        if pw[i] in vowel:
            pw_01.append("0")
        else:
            pw_01.append("1")

    pw_01 = "".join(map(str, pw_01))

    if "000" in pw_01 or "111" in pw_01:
        print(f"<{pw}> is not acceptable.")
        continue

    # e, o 제외 같은글자연속 안됨
    for i in range(len(pw) - 1):
        if (pw[i] == pw[i + 1]) and (pw[i] != "e") and (pw[i] != "o"):
            print(f"<{pw}> is not acceptable.")
            break
    else:
        print(f"<{pw}> is acceptable.")