def solution(survey, choices):
    answer = ""

    # pdb = dict(A=0,C=0,F=0,J=0,N=0,R=0, T=0)

    pdb = {"A": 0, "C": 0, "F": 0, "J": 0, "M": 0, "N": 0, "R": 0, "T": 0}

    for i, s in enumerate(survey):
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            pdb[s[0]] += choices[i]
        else:
            pdb[s[1]] += choices[i] - 4

    if pdb["R"] >= pdb["T"]:
        answer += "R"
    else:
        answer += "T"

    if pdb["C"] >= pdb["F"]:
        answer += "C"
    else:
        answer += "F"

    if pdb["J"] >= pdb["M"]:
        answer += "J"
    else:
        answer += "M"

    if pdb["A"] >= pdb["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
