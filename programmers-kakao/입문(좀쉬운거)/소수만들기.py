def isprime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


def solution(nums):
    answer = 0
    n = len(nums)
    stri = "dff"
    stri.

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if isprime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer


print(solution([1, 2, 3, 4]))
