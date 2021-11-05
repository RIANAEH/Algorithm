# dfs
answer = 0

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer

def dfs(now, value, numbers, target):
    global answer
    if now == len(numbers):
        if value == target:
            answer += 1
        return
    dfs(now+1, value+numbers[now], numbers, target)
    dfs(now+1, value-numbers[now], numbers, target)
   
# bfs
# from collections import deque

# def solution(numbers, target):
#     return bfs(numbers, target)

# def bfs(numbers, target):
#     result = 0
#     q = deque()
#     q.append(numbers[0])
#     q.append(-numbers[0])
#     for i in range(1, len(numbers)):
#         for j in range(2 ** i):
#             n = q.popleft()
#             q.append(n + numbers[i])
#             q.append(n - numbers[i])
#     while q:
#         n = q.popleft()
#         if n == target:
#             result += 1
#     return result
