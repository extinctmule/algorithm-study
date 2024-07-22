from collections import deque


def solution(queue1, queue2):
    s = sum(queue1) + sum(queue2)

    if s % 2:
        return -1

    goal = s // 2
    q1 = deque(queue1)  # 가능?
    q2 = deque(queue2)

    v = deque()

    for cnt in range(len(q1) * 10):  # len(q1) * 3 - 3
        s1 = sum(q1)  # goal이 있으므로 s2는 구할필요 없다.

        if s1 == goal:
            return cnt
        elif q1 not in v:
            v.append(q1.copy())
            if s1 > goal:
                q2.append(q1.popleft())
            else:
                q1.append(q2.popleft())
        else:
            return -1

    return -1


# print(solution([1, 4], [4, 8]))
# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
