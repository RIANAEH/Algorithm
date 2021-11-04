def solution(board, moves):
    answer = 0
    bucket = []
    board_now = [len(board)-1 for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 and i < board_now[j]:
                board_now[j] = i
    for m in moves:
        m -= 1
        if board_now[m] < len(board):
            if bucket and bucket[-1] == board[board_now[m]][m]:
                answer += 2
                bucket.pop()
            else:
                bucket.append(board[board_now[m]][m])
            board_now[m] += 1
    return answer
