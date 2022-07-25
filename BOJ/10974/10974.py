n = int(input())

def dfs(s):
    if len(s) == n:
        print(*s)
        return
    for i in range(1, n + 1):
        if i not in s:
            dfs(s + [i])

dfs([])