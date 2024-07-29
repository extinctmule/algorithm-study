def solution(today, terms, privacies):
    answer = []

    # termsdict 만들고 terms값갖고와서 사전형태로 정리. 달 int변환주의
    # termsdict = {}
    # for t in terms:
    #     k, v = t.split()
    #     termsdict[k] = int(v)
    termsdict = {
        item[0]: int(item[-2:]) for item in terms
    }  # 약관종류가 모두 한자리고 개월수도 1자리또는 2자리니깐, split도필요없이 이렇게 가능.
    # today = [y,m,d]로 변환
    today = list(map(int, today.split(".")))  # 알아서 05->5로 처리됨

    # privacies y,m,d int리스트로 바꾸고, term에따라 month 더하고나서 12보다크면 년 처리
    for i, item in enumerate(privacies):
        ymd, key = item.split()
        y, m, d = map(int, ymd.split("."))

        m += termsdict[key]

        while m > 12:
            m -= 12
            y += 1
        # 실수1: '유효기간은 개인정보를 보관할 수 있는 달 수를 나타내는 정수이며, 1 이상 100 이하입니다.' 이거체크안하고 무조건 12달이 최대라고 가정하듯 풀어서 y+=1 ..
        # if m > 12:
        #     y += m // 12
        #     m = m % 12  # 실수2: m=24일경우, m=0되는경우 생각못함

        # 그결과랑 1)y 2)m 3)d 비교한후 today보다 크거나 '같으면' append
        if today[0] > y:
            answer.append(i + 1)
        elif today[0] == y:
            if today[1] > m:
                answer.append(i + 1)
            elif today[1] == m:
                if today[2] >= d:
                    answer.append(i + 1)

    # 다 append하고나서 sort(필요없음)
    return answer
