from collections import deque


def solution(queue1, queue2):
    s1, s2 = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)

    goal = (s1 + s2) / 2

    # 모든합 홀수면 return -1
    if (goal * 2) % 2 == 1:
        return -1

    csum = s1

    for i in range(len(q1) * 3):

        if csum == goal:
            return i
        elif csum > goal:
            x = q1.popleft()
            csum -= x
            q2.append(x)
        else:
            x = q2.popleft()
            csum += x
            q1.append(x)

    return -1


print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
