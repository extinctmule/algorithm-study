'''
1:05~x
혼자 못푼 문제
n을 곱해나가며 모든자리수가 1인지를 체크하는게 아니라 1,11,111, ... 이 n의 배수인지를 체크해야함.
'''
import sys

for line in sys.stdin:
    n =int(line)
    ones = 0
    digits=1
    while True:
        ones = ones*10+1
        ones %= n
        
        if ones==0:
            print(digits)
            break
        
        digits+=1