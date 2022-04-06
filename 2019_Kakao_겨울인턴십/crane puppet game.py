from collections import defaultdict, deque

'''
스택을 이용하는 문제

n*n 크기 배열이 필요 -> board
인형이 없는 칸은 빈 칸.
같은 모양 인형이 두 개 연속 담기면 삭제. -> stack 형태로 삭제해야 그 다음도 체크 가능
'''
board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    stack = deque()
    result = 0
    # 몇 번 열을 뽑을 지
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] == 0:
                continue
            else:
                stack.append(board[i][m - 1])
                board[i][m - 1] = 0
                while len(stack) >= 2 and stack[-2] == stack[-1]:
                    print(stack.pop())
                    print(stack.pop())
                    print(f"i = {i}, m = {m}")
                    result += 2
                break
    return result


print(solution(board, moves))
