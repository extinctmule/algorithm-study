# 1시 28분
# 바구니는 충분히 크다.
# input: 2차원배열board, 크레인작동시킨 열 순서대로moves
# output: 터뜨려져 사라진 인형개수

# 예상 주의점: 인형이 없는 곳에서 크레인 작동시키는경우 스택추가x 주의
# 인덱스 0시작으로 하자. moves의 원소를 -1해서 쓰는 게 좋겠다!!
from collections import deque


def solution(board, moves):
    answer = 0
    N = len(board)
    cols = [deque() for _ in range(N)]
    bag = []

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                cols[j].append(board[i][j])

    # for i in range(N):
    #     cols[i] = board[:][i]#안됨.이렇게하면 board==cols 됨
    # print(cols)

    for m in moves:
        if cols[m - 1]:  # -1 중요
            val = cols[m - 1].popleft()
            if bag and val == bag[-1]:  # 주의: bag는 스택.
                answer += 2
                bag.pop()
            else:
                bag.append(val)

    return answer


solution(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4],
)
