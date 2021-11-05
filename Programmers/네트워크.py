def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, computers, visited)
    return answer
    
def dfs(now, computers, visited):
    visited[now] = True
    for i in range(len(computers)):
        if computers[now][i] == 1 and not visited[i]:
            dfs(i, computers, visited)
