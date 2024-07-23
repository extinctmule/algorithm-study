res = 0
credit = 0
grade = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0":1.0, "F":0.0}

for _ in range(0,20):
    line = input().split()
    if line[2]=='P':
        continue
    credit +=float(line[1])
    res += float(line[1])*grade[line[2]]
    
print(res/credit)