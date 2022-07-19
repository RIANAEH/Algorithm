from collections import deque

n = int(input())
m = int(input())

# 딕셔너리로 만들어보기!
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    g1, g2 = map(int, input().split());
    graph[g1].append(g2)
    graph[g2].append(g1)

visited = [False] * (n + 1)
queue = deque([1])
visited[1] = True
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
print(visited.count(True) - 1)
