# 시간복잡도를 고려할 필요가 거의 없음. 항상 9줄, 항상 100이하의 수
def imposter(dwarfs,num):
    for i in range(8):
        tmp = num-dwarfs[i]
        if tmp>0:
            for j in range(i+1,9):
                if tmp == dwarfs[j]:
                    return dwarfs[i],dwarfs[j]# i,j 라고 처음에 실수함

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

num = sum(dwarfs)-100
a, b = imposter(dwarfs,num)

for d in dwarfs:
    if d!=a and d!=b:
        print(d)
        
print("\n".join(map(str,dwarfs)))