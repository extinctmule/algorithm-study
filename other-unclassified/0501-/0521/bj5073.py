# 먼저 처리할 것부터 정하자
# 0 0 0 들어오면 출력없이 break
# 그외에는 무조건 양의 정수3개라고 했음
# 세변길이 모두 같은 경우 Equilateral
# else: 길이대로! 오름차순 정렬.
# 두변 같은경우 invalid 확인할필요도 없이 Isosceles출력.
# elif: a+b<=c 이면 invalid.
while True:
    tri = list(map(int, input().split()))
    if tri[0] == 0:
        break

    if tri[0] == tri[1] == tri[2]:  # 이거 파이썬에서 되나?
        print("Equilateral")
    else:
        tri.sort()

        if tri[0] + tri[1] <= tri[2]:
            print("Invalid")
        elif tri[0] == tri[1] or tri[1] == tri[2]:
            print("Isosceles")
        else:
            print("Scalene")
