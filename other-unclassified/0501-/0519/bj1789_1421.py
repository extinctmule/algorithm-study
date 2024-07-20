import sys
sys.stdin = open("input1789.txt")

T = int(input())
for i in range(1, T+1):
    S = int(input())

    cur =1
    for i in range(2,S+2):
        cur+=i
        
        if cur>S:
            print(i-1)
            break

            #print(f"S:{S}, N:{i-1}")
